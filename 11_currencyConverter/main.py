import tkinter as tk
import tkinter.ttk as ttk
import requests
import json
import datetime

curr_date = datetime.date.today()
# print(date.split("-").join())
curr_date = "".join(str(curr_date).split("-"))

curr_raw = requests.get(f"https://data.kurzy.cz/json/meny/b[6]den[{curr_date}]cb[volat].js")
curr_json = json.loads(curr_raw.text[6:-2])

curr_list = ["AUD","BRL","GBP","BGN","CNY","DKK","EUR","PHP","HKD","INR","IDR","ISK","ILS","JPY","ZAR",
            "KRW","CAD","HUF","MYR","MXN","XDR","NOK","NZD","PLN","RON","SGD","SEK","CHF","THB","TRY","USD", "CZK"]

for i in range(len(curr_list)-1):
    curr_rate = curr_json["kurzy"][f"{curr_list[i]}"]["dev_stred"]
    print(f"exchange rate for {curr_list[i]} is", end=" ")
    print(curr_rate)
    
def swap():
    global input_curr
    global output_curr
    input_curr, output_curr = output_curr, input_curr
def calculate():
    global exchange_rate
    global exchange_result
    global input_curr
    global output_curr
    global output_amount
    global input_amount
    if output_curr == "CZK":
        exchange_rate = str(1/float(curr_json["kurzy"][f"{input_curr}"]["dev_stred"]))
    else:
        exchange_rate = curr_json["kurzy"][f"{output_curr}"]["dev_stred"]
    exchange_result = f"result: {input_amount} {input_amount} is {output_amount} {output_amount}"
def dropbox_change(event):
    print("dropbox changed")    

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
default_curr = curr_list[6]
input_curr = "CZK"
output_curr = default_curr
exchange_rate = curr_json["kurzy"][f"{output_curr}"]["dev_stred"]
exchange_result = ""

input_amount = 0
output_amount = 0

label_title = ttk.Label(main_win, text = "Main title:")
label_entry = ttk.Label(main_win, text = f"Exchange {input_curr} to {output_curr}:")
label_dropbox = ttk.Label(main_win, text = f"Choose output currency:")
label_units = ttk.Label(main_win, text = f"{output_curr}")
label_info = ttk.Label(main_win, text = f"xhange rate: {exchange_rate}, {exchange_result}")


# entry widgets, used to take entry from user
enter_curr = ttk.Entry(main_win)

dropbox = ttk.Combobox(main_win, text =curr_list[6],values=curr_list)

btn_swap = ttk.Button(text = "Swap currencies", command=swap)
btn_calc = ttk.Button(text = "Calculate", command=calculate)


# layout using layout manager
label_title.grid(column=layout.currCol(),   row = layout.currRow(), columnspan=layout.spanCol(666), sticky = tk.W, pady = 2)

label_entry.grid(column=layout.setCol(0),   row = layout.nextRow(), sticky = tk.W, pady = 2)
enter_curr.grid(column=layout.nextCol(),    row = layout.currRow(), sticky = tk.W, pady = 2)
label_units.grid(column=layout.nextCol(),   row = layout.currRow(), sticky = tk.W, pady = 2)

label_info.grid(column=layout.setCol(0),    row = layout.nextRow(), columnspan=layout.spanCol(666), sticky = tk.W, pady = 2)

label_dropbox.grid(column=layout.setCol(0),    row = layout.nextRow(), sticky = tk.W, pady = 2)
dropbox.grid(column=layout.nextCol(),    row = layout.currRow(), sticky = tk.W, pady = 2)

btn_swap.grid(column=layout.setCol(0),      row = layout.nextRow(), sticky = tk.W, pady = 2)
btn_calc.grid(column=layout.nextCol(),      row = layout.currRow(), sticky = tk.E, pady = 2)

# TODO: make next dropbox

dropbox.bind('<<ComboboxSelected>>', dropbox_change)


# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)
 
# # infinite loop which can be terminated by keyboard
# # or mouse interrupt
tk.mainloop()

#TODO make curr_list converter which connects on the internet and gather data through some API
    # EURO, CZK, USD, GBP, KRW