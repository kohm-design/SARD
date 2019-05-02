import sys, os, math
#'''Coordinate format type:
 #   1) DMS: dd mm'ss.s N"
  #  2) DMM: dd mm.mmmmm
   # 3) DD: dd.ddddd
#
 #   Lat: -90 to +90
  #  Lon: -180 to +180'''

#def check_input(s)
 #   if(s.

#def convert_style(coords, style)

RADIUS_MILE_EARTH = 3958.8
LON_CIRCUMFERENCE_FEET_EARTH = 24860*5280
LAT_FEET_DEGREES = LON_CIRCUMFERENCE_FEET_EARTH/360

def lon_feet_degrees(lat):
    radius_lat = 5280*math.cos(abs(lat))*RADIUS_MILE_EARTH
    return radius_lat*math.pi/180

def gen_waypoints(x1,y1,x2,y2,space=50, mode=0):
    #lenx = abs(x2-x1)
    #leny = abs(y2-y1)
    A =[]

    #convert space to degrees
    dy = min((space/lon_feet_degrees(x1)),(space/lon_feet_degrees(x2))) #smallest degree is largest side
    dx = space/LAT_FEET_DEGREES
    

    #Generate Waypoint List
    tempx = x1
    tempy = y1

    if(mode == 0): #search north to south
        if(y1>y2):
            while((tempy>=y2)):
                if(tempx==x1):            
                    A.extend([tempx,tempy])
                    tempx = x2
                    A.extend([tempx,tempy])

                elif(tempx==x2):
                    A.extend([tempx,tempy])
                    tempx = x1
                    A.extend([tempx,tempy])
                    
                tempy = tempy - dy
                if(tempy <=y2):
                    tempy = y2

                if((tempy == y2)and(tempx == x2)):
                    break

        else:
            while((tempy<=y2)):
                if(tempx==x1):            
                    A.extend([tempx,tempy])
                    tempx = x2
                    A.extend([tempx,tempy])

                elif(tempx==x2):
                    A.extend([tempx,tempy])
                    tempx = x1
                    A.extend([tempx,tempy])
                    
                tempy = tempy + dy
                if(tempy >=y2):
                    tempy = y2

                if((tempy == y2)and(tempx == x2)):
                    break

    elif(mode==1): #search East to West
        if(x1>x2):
            while((tempx>=x2)):
                if(tempy==y1):            
                    A.extend([tempx,tempy])
                    tempy = y2
                    A.extend([tempx,tempy])

                elif(tempy==y2):
                    A.extend([tempx,tempy])
                    tempy = y1
                    A.extend([tempx,tempy])
                    
                tempx = tempx - dx
                if(tempx <=x2):
                    tempx = x2

                if((tempy == y2)and(tempx == x2)):
                    break

        else:
            while((tempx<=x2)):
                if(tempy==y1):            
                    A.extend([tempx,tempy])
                    tempy = y2
                    A.extend([tempx,tempy])

                elif(tempy==y2):
                    A.extend([tempx,tempy])
                    tempy = y1
                    A.extend([tempx,tempy])
                    
                tempx = tempx + dx
                if(tempx >=x2):
                    tempx = x2

                if((tempy == y2)and(tempx == x2)):
                    break
                
    
    # Return waypoint list
    return A

#Write Waypoints to file
def write_waypoints_to_file(A,filepath='test_waypoint.txt'):
    try:
        f= open(filepath,'w')
        i=0
        while (i<len(A)):
            f.write(str(A[i])+' '+str(A[i+1]) +'\n')
            i+=2        
    finally:
        f.close()
    return

def load_waypoints_from_file(filepath='test_waypoint.txt'):
    A=[]
    try:
        f= open(filepath)
        for line in f:
            x=line.split()
            if(check_input_coord(x[0],'lat') and check_input_coord(x[1],'lon')):
                A.extend(x)
    finally:
        f.close()
    return A

def check_input_coord(s,mode='lat'):
    s = s.strip()
    s1 = s.replace('.','',1)
    s1= s1.replace('-','',1)
       
        
    if(not(s1.isdecimal())):
        return False

    x=float(s)
    if(mode =='lat'):
        if((x >90)or(x<-90)):
            return False
    elif(mode =='lon'):
        if((x>180)or(x<-180)):
            return False

    return True

def check_spacing(s):
    s = s.strip()
    s1 = s.replace('.','',1)
    s1= s1.replace('-','',1)

    if(not(s1.isdecimal())):
        return False
    x=float(s)
    if((x<=0)or(x>1000000)): #don't need huge numbers
        return False

    return True

#x1 =30.62
#y1 = -96.34

#x2 = 30.61
#y2 = -96.31

#A=gen_waypoints(x1,y1,x2,y2,100,1)
#write_waypoints_to_file(A)
