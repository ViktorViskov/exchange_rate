#!/usr/bin/python3

#GUI for parser program

# 
# import libs
# 
import tkinter, parser


# 
# app
# 

# create main window
root = tkinter.Tk(className="exchange rate")

# block to resize
root.resizable(0, 0)

# create inout field 1
input_field1 = tkinter.Entry(root, width=4, bg="white")
# put default value
input_field1.insert("end", "btc")
# item position
input_field1.grid(row=0, column=0)

# create inout field 1
input_field2 = tkinter.Entry(root, bg="white", width=4)
# put default value
input_field2.insert("end", "usd")
# item position
input_field2.grid(row=1, column=0)

# create label
label = tkinter.Label(root)
# label position
label.grid(row=0, column=1)

# create button and put lambda function to action
btn = tkinter.Button(root, text="Get", command=lambda: label.config(text=parser.parseData(input_field1.get(), input_field2.get())))
# button position
btn.grid(row=1, column=1)

# show window
root.mainloop()

