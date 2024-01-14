import tkinter as tk
import tkinter.ttk as ttk
import requests
import json

curr_raw = requests.get("https://data.kurzy.cz/json/meny/b[6]den[20211111]cb[volat].js")
curr_json = json.loads(curr_raw.text[6:-2])

curr_list = ["AUD","BRL","GBP","BGN","CNY","DKK","EUR","PHP","HKD","INR","IDR","ISK","ILS","JPY","ZAR",
            "KRW","CAD","HUF","MYR","MXN","XDR","NOK","NZD","PLN","RON","SGD","SEK","CHF","THB","TRY","USD"]

for i in range(len(curr_list)):
    curr_rate = curr_json["kurzy"][f"{curr_list[i]}"]["dev_stred"]
    print(f"exchange rate for {curr_list[i]} is", end=" ")
    print(curr_rate)
    
def rename():
    global l1
    l1["text"] = ""

class LayoutManager:
    def __init__(self) -> None:
        self.rows = 0
        self.cols = 0
    def newRow(self):
        self.rows += 1
        return self.rows
    def newCol(self):
        self.cols += 1
        return self.cols
    def currCol(self):
        return self.cols
    def currRow(self):
        return self.rows

layout = LayoutManager()

# creating main tkinter window/toplevel
main_win = tk.Tk()
main_win.title("Curr_list converter")


# this will create a label widget
l1 = ttk.Label(main_win, text = "First:")
l2 = ttk.Label(main_win, text = "Second:")
l3 = ttk.Label(main_win, text = "Third:")
l4 = ttk.Label(main_win, text = "Fourth:")

# entry widgets, used to take entry from user
e1 = ttk.Entry(main_win)
e2 = ttk.Entry(main_win)

drop_list = ttk.Combobox(main_win, textvariable=curr_list[6],values=curr_list)

btn1 = ttk.Button(text = "change", command=rename)

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = layout.currRow(), column = layout.currCol(), columnspan=30, sticky = tk.W, pady = 2)
l2.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)
l3.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)
l4.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)
e1.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)
e2.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)
btn1.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)
drop_list.grid(row = layout.newRow(), column = layout.newCol(), sticky = tk.W, pady = 2)




# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)
 
# # infinite loop which can be terminated by keyboard
# # or mouse interrupt
tk.mainloop()

#TODO make curr_list converter which connects on the internet and gather data through some API
    # EURO, CZK, USD, GBP, KRW