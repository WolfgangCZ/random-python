import tkinter

window = tkinter.Tk()

win_width = 500
win_height = 500

while True:

    window.title("test")
    window.minsize(width=win_width, height=win_height)

    my_button = tkinter.Button(text="button")
    my_button.pack()

    my_frame = tkinter.Frame()
    my_frame.pack()


    my_label = tkinter.Label(text="label", font=("Arial", 24, "bold"))
    my_label.pack()

    window.mainloop()