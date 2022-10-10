import tkinter as tk

window = tk.Tk()
#generic window size, showing listbox is smaller than window
window.geometry("600x480")

frame = tk.Frame(window)
frame.pack()

listBox = tk.Listbox(frame, width=20, height=5, selectmode='multiple')
listBox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=listBox.yview)
scrollbar.pack(side="right", fill="y")

listBox.config(yscrollcommand=scrollbar.set)

listBox.insert('end', 'Python')
listBox.insert('end', 'C')
listBox.insert('end', 'C++')
listBox.insert('end', 'SQl')
listBox.insert('end', 'Java')
listBox.insert('end', 'HTML')
listBox.insert('end', 'CSS')
listBox.insert('end', 'Java Script')
listBox.insert('end', 'OOPs')

def select(event=None):
    output = []
    selection = listBox.curselection()
    #.curselection() returns a list of the indexes selected
    #need to loop over the list of indexes with .get()
    for i in selection:
        o = listBox.get(i)
        output.append(o)
    print((" ").join(output))


listBox.bind('<Button>', select)

window.mainloop()