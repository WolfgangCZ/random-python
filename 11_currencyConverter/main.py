import tkinter as tk
import tkinter.ttk as ttk
import requests
import json
import datetime

curr_date = datetime.date.today()
# print(date.split("-").join())
curr_date = "".join(str(curr_date).split("-"))

curr_raw = requests.get(f"https://data.kurzy.cz/json/meny/b[6]den[{curr_date}]cb[volat].js")
curr_raw = curr_raw.text[6:-4]
curr_raw += ',"CZK":{"jednotka":1,"dev_stred":1,"dev_nakup":null,"dev_prodej":null,"val_stred":null,"val_nakup":null,"val_prodej":null,"nazev":"Americk\u00FD dolar","url":"https://www.kurzy.cz/usd"}}}'
curr_json = json.loads(curr_raw)


curr_list = []

for curr in curr_json["kurzy"]:
    curr_list.append(curr)
    print(curr)

def update():
    global label_info
    global exchange_rate
    exchange_rate = float(curr_json["kurzy"][f"{output_curr}"]["dev_stred"])/float(curr_json["kurzy"][f"{input_curr}"]["dev_stred"])
    label_info.configure(text=f"Exchange rate {input_curr} to {output_curr} is {exchange_rate:.2f} today")


def swap():
    global input_curr
    global output_curr
    input_curr, output_curr = output_curr, input_curr
    dropbox_in.current(curr_list.index(input_curr))
    dropbox_out.current(curr_list.index(output_curr))
    update()
    

def calculate():
    update()
    global exchange_rate
    global exchange_result
    global input_curr
    global output_curr
    global input_amount
    global output_amount
    global label_result
    try:
        input_amount = float(enter_curr.get())
        output_amount = float(input_amount)/float(exchange_rate)
        exchange_result = f"result: {input_amount:.2f} {input_curr} is {output_amount:.2f} {output_curr}"
        label_result.configure(text = exchange_result)
    except:
        print("error")
        label_result.configure(text = "ERROR: Incorrect input! Has to be a number")    
    

def dropbox_change(event):
    global dropbox_in
    global dropbox_out
    global input_curr
    global output_curr
    global curr_list
    input_curr = dropbox_in.get()
    output_curr = dropbox_out.get()
    update()

class LayoutManager:
    def __init__(self) -> None:
        self.col = 0
        self.row = 0
    def nextCol(self):
        self.col += 1
        return self.col
    def nextRow(self):
        self.row += 1
        return self.row
    def setCol(self, pos: int):
        self.col = pos
        return self.col
    def setRow(self, pos: int):
        self.row = pos
        return self.row
    def currCol(self):
        return self.col
    def currRow(self):
        return self.row
    def spanCol(self, span: int):
        self.col += span - 1
        return span + 1
    def spanRow(self, span: int):
        self.row += span - 1
        return span

layout = LayoutManager()

main_win = tk.Tk()
main_win.title("Curr_list converter")
input_curr = curr_list[6]
output_curr = curr_list[-1]
exchange_rate = curr_json["kurzy"][f"{output_curr}"]["dev_stred"]
exchange_result = ""

input_amount = 0
output_amount = 0

label1 = ttk.Label(main_win, text = "From: ")
label2 = ttk.Label(main_win, text = " to: ")
label3 = ttk.Label(main_win, text = " amount: ")
label_info = ttk.Label(main_win, text = f"Exchange rate {input_curr} to {output_curr} is {exchange_rate} today")
label_result = ttk.Label(main_win, text = f"")



dropbox_in = ttk.Combobox(main_win, values=curr_list)
dropbox_out = ttk.Combobox(main_win, values=curr_list)

# entry widgets, used to take entry from user
enter_curr = ttk.Entry(main_win)

btn_swap = ttk.Button(text = "Swap currencies", command=swap)
btn_calc = ttk.Button(text = "Calculate", command=calculate)


# layout using layout manager

label1.grid(     column=layout.setCol(0),   row = layout.currRow(), sticky = tk.W, pady = 2)
dropbox_in.grid( column=layout.nextCol(),   row = layout.currRow(), sticky = tk.W, pady = 2)
label2.grid(     column=layout.nextCol(),   row = layout.currRow(), sticky = tk.W, pady = 2)
dropbox_out.grid(column=layout.nextCol(),   row = layout.currRow(), sticky = tk.W, pady = 2)
label3.grid(     column=layout.nextCol(),   row = layout.currRow(), sticky = tk.W, pady = 2)
enter_curr.grid( column=layout.nextCol(),   row = layout.currRow(), sticky = tk.W, pady = 2)

label_info.grid(column=layout.setCol(0),    row = layout.nextRow(), columnspan=layout.spanCol(666), sticky = tk.W, pady = 2)
label_result.grid(column=layout.setCol(0),    row = layout.nextRow(), columnspan=layout.spanCol(666), sticky = tk.W, pady = 2)


btn_swap.grid(column=layout.setCol(6),      row = layout.nextRow(), sticky = tk.W, pady = 2)
btn_calc.grid(column=layout.nextCol(),      row = layout.currRow(), sticky = tk.E, pady = 2)

dropbox_in.current(6)
dropbox_out.current(len(curr_list)-1)


dropbox_in.bind('<<ComboboxSelected>>', dropbox_change)
dropbox_out.bind('<<ComboboxSelected>>', dropbox_change)


# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)
 
# # infinite loop which can be terminated by keyboard
# # or mouse interrupt
update()
tk.mainloop()

#TODO make curr_list converter which connects on the internet and gather data through some API
    # EURO, CZK, USD, GBP, KRW