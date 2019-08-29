from tkinter import *
#from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        #change title of master widget
        self.master.title("test window")

        #allow widget to take full root window
        self.pack(fill=BOTH, expand=1)

        #create button instance
        #quitButton = Button(self, text="Quit", command = self.client_exit)

        # place button on widget
        #quitButton.place(x=100, y=150)

        tst_menu = Menu(self.master)
        self.master.config(menu=tst_menu)

        file = Menu(tst_menu)

        file.add_command(label = "Exit", command=self.client_exit)

        tst_menu.add_cascade(label="File", menu=file)

        edit = Menu(tst_menu)
        edit.add_command(label = "Undo")
        tst_menu.add_cascade(label="Edit", menu=edit)


         # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
  #      edit.add_command(label="Show Img", command=self.showImg)
   #     edit.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        #tst_menu.add_cascade(label="Edit", menu=edit)

    #def showImg(self):
     #   load = Image.open("73599893.jpg")
      #  render = ImageTk.PhotoImage(load)

        # labels can be text or images
       # img = Label(self, image=render)
        #img.image = render
        #img.place(x=0, y=0)


    #def showText(self):
      #  text = Label(self, text="Hey there good lookin!")
     #   text.pack()

    def client_exit(self):
        exit()
        
        
root = Tk()

#size of window
root.geometry("400x300")


app = Window(root)
root.mainloop()
