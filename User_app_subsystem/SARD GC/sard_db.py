import pymongo
from mongoengine import *

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["waypoints"]
#mycol = mydb["home"]

#myway = {"Longitude": 177.46, "Latitude": 31.43 }

#x = mycol.insert_one(myway)

#print(myclient.list_database_names())
#print(mydb.list_collection_names())

connect('sard_db')

#Define Waypoint class
class WaypointsDB(Document):
    index = IntField(min_value=0, max_value=None, primary_key = True, default = WaypointsDB.count_documents({}) )
    latitude = DecimalField(min_value=-90, max_value=90, precision=7)
    longitude = DecimalField(min_value=-180, max_value=180, precision=7)
    altitude = DecimalField(min_value=0)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

  #  def UpdateIndex():
    #    if WaypointsDB.count_documents({}) <= 0:
      #      return 0
        #else:
          #  return WaypointsDB.count_documents({})

class ImageDB(Document):
    index =IntField(min_value=0, max_value=None, primary_key = True, default = ImageDB.count_documents({}))
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

   # def UpdateIndex():
     #   if ImageDB.count_documents({}) <= 0:
       #     return 0
        #else:
          #  return ImageDB.count_documents({})


test = WaypointsDB( latitude= 31.765, longitude= -91.3675785412, altitude=100).save()
test = WaypointsDB( latitude= 31.765, longitude= -91.3675785412, altitude=100).save()
test = ImageDB( ).save()
test = ImageDB( ).save()
