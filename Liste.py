from tkinter import*
import dbm

root = Tk()
db = dbm.open("cache", "c")
dbm.writelines(Liste)

def get_list():
        
        index = listbox1.curselection()[0]
        seltext = listbox1.get(index)
        enter1.delete(0, 50)
        enter1.insert(0, seltext)        
    
        
def add_item():
        listbox1.insert(END, enter1.get())
        
def delete_item():
        try:
                index = listbox1.curselection()[0]
                listbox1.delete(index)
        except IndexError:
                pass     
        

listbox1 =Listbox(root, width=20, height=10)
listbox1.grid(row=0, column=0)

yscroll = Scrollbar(command=listbox1.yview, orient=VERTICAL)
yscroll.grid(row=0, column=1, sticky=N+S)
listbox1.configure(yscrollcommand=yscroll.set)

enter1 = Entry(root, width=20)
enter1.insert(0, '')
enter1.grid(row=1, column=0)

button = Button(root, text='Ajouter', command=add_item)
button.grid(row=2, column=0, sticky=W)

button1 = Button(root, text='Supprimer', command=delete_item)
button1.grid(row=2, column=0, sticky=E)

root.mainloop()
