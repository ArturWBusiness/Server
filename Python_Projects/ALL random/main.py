from tkinter import *

root = Tk()
root.geometry("1280x720")


def startProgram(shapefile_path):
    text.insert('1.0', "Button has ben clicked!")

text = Text(root, height=8, width=25)
text.grid(row=10, column=0, padx=20, pady=5)

label = Label(root, text="Status",font=12)
label.grid(row=9, column=0, padx=5, pady=5)


button2=Button(root,text="Start Program", width=20,font=12,command=lambda:     startProgram(0))
button2.grid(row=7, column=0, padx=20, pady=10)

button3=Button(root, text='Exit Program',    width=20,font=12,command=root.destroy)
button3.grid(row=8, column=0,padx=20, pady=10)

root.mainloop()