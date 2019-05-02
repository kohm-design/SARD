from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from goompy import GooMPy
from sard_map import*
from SARD_Funct import*
from sard_dialogs import*
import sys, os

#Constants for Map
WIDTH = 800
HEIGHT = 500

RADIUS = None
NTILES= 100
LATITUDE  =  30.621040
LONGITUDE =  -96.339277
ZOOM = 7
MAPTYPE = 'hybrid'

#Window Class
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        #variables
        waypoints =[] #waypoint list
        filename ='' #filename to load or save to.

        #change title of master widget
        self.master.title("SARD_Window")

        #allow widget to take full root window
        #self.pack(fill=BOTH, expand=1)

        #Menus
        tst_menu = Menu(self.master)
        self.master.config(menu=tst_menu)

        #file Menu
        file = Menu(tst_menu)
        file.add_command(label = "Load Waypoints", command=self.open_waypoints)
        file.add_command(label = "Save Waypoints", command=self.save_waypoints)
        file.add_command(label = "Change Image Directory")#, command=self.client_directory)
        file.add_command(label = "Start/Abort Mission")#, command=self.client_start) #todo
        file.add_command(label = "Exit", command=self.client_exit)
            
        tst_menu.add_cascade(label="File", menu=file)

        #View Menu
        view = Menu(tst_menu)
        view.add_command(label = "Toggle Path")#, command=self.path_toggle)
        view.add_command(label="Toggle Images")#, command=self.image_toggle)
        view.add_command(label="Toggle Location")#, command=self.location_toggle)
        view.add_command(label="Open Gallery")#, command=self.open_gallery)
        view.add_command(label="Waypoint List", command=self.pop_waypoint)

        tst_menu.add_cascade(label="View", menu=view)

        #map frame instantiation
        map_frame = MAP()
        map_frame.grid(row = 0, column = 10, columnspan = 100, rowspan = 100, sticky = 'E', padx = 25)
        map_frame.bind('<Button-1>', lambda: self.click_pass(map_frame,event))
        map_frame.bind('<B1-Motion>',lambda: self.drag_pass(map_frame,event))

        #Update map coords
        Label(self.master, text='Change Map Coordinates').grid(row = 0, column=0, columnspan = 10)
        e1 = Entry(self.master)
        e2 = Entry(self.master)
        e1.grid(row =1, column =1)
        e2.grid(row = 2, column =1)
        Label(self.master, text='Latitude:').grid(row = 1, column=0, sticky = 'W')
        Label(self.master, text='Longitude:').grid(row = 2, column=0, sticky = 'W')
        bUP = Button(self.master, text = 'Update Map', command = lambda : self.update_coords(e1.get(),e2.get(), map_frame))
        bUP.grid( row =3,column =0,sticky='e' )
            #set Home coordinate
        home = []
        homeUP = Button(self.master, text = 'Update Home', command = lambda : self.home_coords(e1.get(),e2.get(), map_frame))
        homeUP.grid( row =3,column =1)

        #Generate waypoints
        genmode = IntVar()
        genmode.set(0)
        Label(self.master, text='Generate Waypoints').grid(row = 4, column=0, columnspan = 10)
            #Coord1
        e3 = Entry(self.master)
        e4 = Entry(self.master)
        e3.grid(row =5, column =1)
        e4.grid(row = 6, column =1)
        Label(self.master, text='Latitude 1:').grid(row = 5, column=0, sticky = 'W')
        Label(self.master, text='Longitude 1:').grid(row = 6, column=0, sticky = 'W')
            #coord2
        e5 = Entry(self.master)
        e6 = Entry(self.master)
        e5.grid(row =7, column =1)
        e6.grid(row = 8, column =1)
        Label(self.master, text='Latitude 2:').grid(row = 7, column=0, sticky = 'W')
        Label(self.master, text='Longitude 2:').grid(row = 8, column=0, sticky = 'W')
            #spacng between points
        e7 = Entry(self.master)
        e7.grid(row =9, column =1)
        Label(self.master, text='Spacing (feet)').grid(row = 9, column=0, sticky = 'W')
        
            #mode selector
        Label(self.master, text='Mode:').grid(row = 10, column=0, sticky = 'W')
        Radiobutton(self.master, text='N/S', variable=genmode, value =0).grid(row =10,column=1)
        Radiobutton(self.master, text='E/W', variable=genmode, value =1).grid(row =10,column=2)
            #generate points
        gen = Button(self.master, text = 'Generate', command = lambda : self.generate_coords(e3.get(),e4.get(), e5.get(),e6.get(),e7.get(), genmode.get(), map_frame))
        gen.grid( row =11,column =0, columnspan=10)


        #Start/Stop Mission
        
    ''' #File Menu Commands ToDo
    def client_load(self):
    def client_save(self):
    def client_directory(self):
    def client_start(self):   '''

    def client_exit(self):
        exit(0)

    '''#View Menu Commands ToDo
    def path_toggle(self):
    def image_toggle(self):
    def location_toggle(self):
    def open_gallery(self):'''

    #Map Functions
    def update_coords(self,s1,s2, map_frame):
        e=''
        s1 = s1.strip()
        s2 = s2.strip()
        
        if((not(check_input_coord(s1,'lat')))or (not(check_input_coord(s2,'lon')))):
            if(not(check_input_coord(s1,'lat'))):
                e= e+'Latitude should be between -90 and 90 degrees.\n'
            if(not(check_input_coord(s2,'lon'))):
                e= e+'Longitude should be between -180 and 180 degrees.\n'
            self.warn_pop(e)
            return
        
        lat = float(s1)
        lon = float(s2)
        
        map_frame.update_coords_map(lat,lon)


    def generate_coords(self, s1, s2, s3, s4, s5, mode, map_frame):
        e=''
        space =100
        s1 = s1.strip()
        s2 = s2.strip()
        s3 = s3.strip()
        s4 = s4.strip()
        s5 = s5.strip()
        #print(str(mode))
        
        if((not(check_input_coord(s1,'lat')))or (not(check_input_coord(s2,'lon')))or(not(check_input_coord(s3,'lat')))or (not(check_input_coord(s4,'lon')))):
            if(not(check_input_coord(s1,'lat'))):
                e= e+'Latitude 1 should be between -90 and 90 degrees.\n'
            if(not(check_input_coord(s2,'lon'))):
                e= e+'Longitude 1 should be between -180 and 180 degrees.\n'
            if(not(check_input_coord(s3,'lat'))):
                e= e+'Latitude 2 should be between -90 and 90 degrees.\n'
            if(not(check_input_coord(s4,'lon'))):
                e= e+'Longitude 2 should be between -180 and 180 degrees.\n'
            self.warn_pop(e)
            return

        if(not(check_spacing(s5))):
            e = 'Spacing should be greater than 0 and less than 1000000.\n Default of 100 ft used.\n'
            self.warn_pop(e)
            space = 100
        else:
            space = float(s5)
        
        x1 = float(s1)
        y1 = float(s2)
        x2 = float(s3)
        y2 = float(s4)
        self.waypoints = gen_waypoints(x1,y1,x2,y2, space, mode)
        #write_waypoints_to_file(A,filepath='waypoint_list.txt')

    def home_coords(self,s1,s2, map_frame):
        e=''
        s1 = s1.strip()
        s2 = s2.strip()
        
        if((not(check_input_coord(s1,'lat')))or (not(check_input_coord(s2,'lon')))):
            if(not(check_input_coord(s1,'lat'))):
                e= e+'Latitude should be between -90 and 90 degrees.\n'
            if(not(check_input_coord(s2,'lon'))):
                e= e+'Longitude should be between -180 and 180 degrees.\n'
            self.warn_pop(e)
            return
        self.home=[s1,s2]
        lat = float(s1)
        lon = float(s2)
        
        map_frame.update_coords_map(lat,lon)
    
    def drag_pass(self,map_frame, event):
        map_frame.drag(event)

    def click_pass(self,map_frame, event):
        map_frame.click(event)

    #error Popup
    def warn_pop(self,s) :
        messagebox.showwarning("Warning", "%s\n" %s)

    #file management
    def open_waypoints(self):
        self.filename = filedialog.askopenfilename(initialdir = "./", title = "Open...")
        if(not(len(self.filename)==0)):
            self.waypoints = load_waypoints_from_file(self.filename)
                

    def save_waypoints(self):
        self.filename = filedialog.asksaveasfilename(initialdir = "./", title = "Save As...", initialfile = self.filename)
        if(not(len(self.filename)==0)):
            write_waypoints_to_file(self.waypoints,self.filename)

    #waypoint popup
    def pop_waypoint(self):
        d = show_waypoints(self,'Waypoints', self.waypoints)
        #wait_window(d.top)

#root.wait_window(d.top)

#def pospress(event) :
#    print ('mouse press Position: (%s %s)' % (event.x, event.y))
#    return
#def posrelease(event) :
#    print ('mouse release Position: (%s %s)' % (event.x, event.y))
#    return
#def motion(event) :
#    print ('Current mouse Position: (%s %s)' % (event.x, event.y))
#    return
        
root = Tk()

#size of window
#root.geometry("1000x500")
#root.bind('<B1-Motion>', motion)
#root.bind('<ButtonRelease-1>', posrelease)
#root.bind('<Button-1>', pospress)
app = Window(root)
root.mainloop()
