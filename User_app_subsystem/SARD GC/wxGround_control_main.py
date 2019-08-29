import gmaps
import wx
apikey = open("GoogleMapsAPIkey.txt",'r').read()
gmaps.configure(api_key=apikey)
new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "SARD") # A Frame is a top-level window.
frame.Show(True)

app.MainLoop()
