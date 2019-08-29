import sys

if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk

from PIL import ImageTk

from goompy import GooMPy

WIDTH = 800
HEIGHT = 500

RADIUS = None
NTILES= 100
LATITUDE  =  30.621040
LONGITUDE =  -96.339277
ZOOM = 12
MAPTYPE = 'hybrid'

class MAP(tk.Frame):

    def __init__(self):

        tk.Frame.__init__(self)

        #self.geometry('%dx%d+500+500' % (WIDTH,HEIGHT))
        #self.title('GooMPy')

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)

        self.canvas.pack()

        #self.bind("<Key>", self.check_quit)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<Button-1>', self.click)

        self.label = tk.Label(self.canvas)

        self.radiogroup = tk.Frame(self.canvas)
        self.radiovar = tk.IntVar()
        self.maptypes = ['roadmap', 'terrain', 'satellite', 'hybrid']
        self.add_radio_button('Road Map',  0)
        self.add_radio_button('Terrain',   1)
        self.add_radio_button('Satellite', 2)
        self.add_radio_button('Hybrid',    3)

        self.zoom_in_button  = self.add_zoom_button('+', +1)
        self.zoom_out_button = self.add_zoom_button('-', -1)

        self.zoomlevel = ZOOM

        maptype_index = 3
        self.radiovar.set(maptype_index)

        self.goompy = GooMPy(WIDTH, HEIGHT, LATITUDE, LONGITUDE, ZOOM, MAPTYPE, RADIUS, NTILES)

        self.restart()

    #def add_zoom_indicator(self,

    def add_zoom_button(self, text, sign):

        button = tk.Button(self.canvas, text=text, width=1, command=lambda:self.zoom(sign))
        return button

    def reload(self):

        self.coords = None
        self.redraw()

        self['cursor']  = ''


    def restart(self):

        # A little trick to get a watch cursor along with loading
        self['cursor']  = 'watch'
        self.after(1, self.reload)

    def add_radio_button(self, text, index):

        maptype = self.maptypes[index]
        tk.Radiobutton(self.radiogroup, text=maptype, variable=self.radiovar, value=index, 
                command=lambda:self.usemap(maptype)).grid(row=0, column=index)

    def click(self, event):

        self.coords = event.x, event.y
        print('coords: %f, %f \n', self.goompy.lat, self.goompy.lon)
    def drag(self, event):

        self.goompy.move(self.coords[0]-event.x, self.coords[1]-event.y)
        self.image = self.goompy.getImage()
        self.redraw()
        #self.coords = event.x, event.y
        print('coords: %f, %f \n', self.goompy.lat, self.goompy.lon)
        print('dx: ', self.coords[0]-event.x,' dy: ',self.coords[1]-event.y)
        self.coords = event.x, event.y

    def redraw(self):

        self.image = self.goompy.getImage()
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.label['image'] = self.image_tk

        self.label.place(x=0, y=0, width=WIDTH, height=HEIGHT) 

        self.radiogroup.place(x=0,y=0)

        x = int(self.canvas['width']) - 50
        y = int(self.canvas['height']) - 80

        self.zoom_in_button.place(x= x, y=y)
        self.zoom_out_button.place(x= x, y=y+30)

    def usemap(self, maptype):

        self.goompy.useMaptype(maptype)
        self.restart()

    def zoom(self, sign):

        newlevel = self.zoomlevel + sign
        if newlevel > 0 and newlevel < 22:
            self.zoomlevel = newlevel
            self.goompy.useZoom(newlevel)
            self.restart()

    def update_coords_map(self, lat, lon):
        self.goompy.lat = lat
        self.goompy.lon = lon
        self.goompy._fetch_and_update()
        self.restart()
