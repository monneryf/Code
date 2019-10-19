from tkinter import Entry, Label, StringVar, Spinbox, Tk

root = Tk()

#root.resizable(False,False)
root.title("Tuto Tkinter")
root.config(bg='silver')

Label(root,text="Enter your name below").pack()
myVar = StringVar()
Entry(root,textvariable=myVar,width=10).pack()

Label(root,text="Pick a color").pack()
my_box = Spinbox(root,from_=4,to=8).pack()

root.mainloop()
