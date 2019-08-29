from tkinter import *
#from Ground_control_main import *
class show_waypoints:

    def __init__(self, parent, title, A):

        top = self.top = Toplevel(parent)

        Label(top, text=title).pack()

        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox = Listbox(top, yscrollcommand=scrollbar.set)
        i=0
        while i <len(A):
            listbox.insert(END, str(A[1])+' '+str(A[i+1]))
            listbox.pack(side=LEFT, fill=BOTH)
            i+=2
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)
        scrollbar.config(command=listbox.yview)

    def ok(self):
        self.top.destroy()



#root = Tk()
#Button(root, text="Hello!").pack()
#root.update()

#d = show_waypoints(root)

#root.wait_window(d.top)
