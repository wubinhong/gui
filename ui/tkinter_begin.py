from tkinter import Label, Tk, Button, StringVar, Frame
from datetime import datetime

root = Tk()


def my_click():
    print('Click logging', datetime.now())
    # label1.labelText = "Click me now! --> " + str(datetime.now())
    # label1.grid(row=0, column=0)
    date_str = str(datetime.now())
    labelText.set('Update Label: ' + date_str)
    label3.config(text=date_str)
    label2.config(text='Label2: ' + date_str)


# Create Label Widget
labelText=StringVar(value="Hello")
label1=Label(root, textvariable=labelText)
label2=Label(root, text="This is my second label")
myBtn1=Button(root, text="Click me!", padx=100, pady=50, command=my_click)
frame=Frame(root)
label3=Label(frame, text="Label in frame")

# Showing it onto the screen
# label1.pack()
# myBtn1.pack()
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
myBtn1.grid(row=2)
frame.grid(row=3)
label3.pack()


root.mainloop()
