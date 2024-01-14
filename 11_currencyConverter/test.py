# Import the required library
from tkinter import *

# Create an instance of tkinter frame or widget
win = Tk()
win.geometry("700x350")

def update_text():
   # Configuring the text in Label widget
   label.configure(text="This is updated Label text")

# Create a label widget
label=Label(win, text="This is New Label text", font=('Helvetica 14 bold'))
label.pack(pady= 30)

# Create a button to update the text of label widget
button=Button(win, text= "Update", command=update_text)
button.pack()

win.mainloop()