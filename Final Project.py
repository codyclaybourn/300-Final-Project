FinalProjectV1.py
# Name:
# Date:
# Code purpose: Do interesting things of little importance
# Import external libraries
import numpy as np
import time
import math
pi = 3.14159265359


# Import internal programs
import L2_vector.py as vector
import L2_log as log
import L2_inverse_kinematics.py as invkin
import L2_kinematics.py as kin
import L1_lidar as lidar
import L2_speed_control as spd
import csv

#takes path data from external csv file and returns populated array
#returns [x global, y global, speed setting, circle radius] 
#A positive radius curves to the left and a negative curves to the right
#Speed settings are 1 through 5, 5 beaing the fastest.
def getArray():
    data=numpy.array([][])
    my_data = numpy.genfromtxt('PathData.csv', delimiter=',')
    return my_data
    

#returns distance of straight line or circle in meters
def distance(x1, y1, x2, y2, theta):
    if theta == 0:                                                                      #calculation for a straight line

    if theta == 0:                                                                      #calculation for a straight line
        length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   
        return length

def distance(x1, y1, x2, y2, theta):
    if theta == 0:                                                                      #calculation for a straight line
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)   
        return dist
        
    else if theta == (pi)/2                                                           # quarter circle
        dist = (math.sqrt((y2 - y1)**2 + (x2 - x1)**2)) / 2*math.sin((pi/2)/2)
        length = (dist*(pi/2)) / quarterArcTime 
        return length 
        
    else if theta == (pi)                                                             # semi circle
        dist = (math.sqrt((y2 - y1)**2 + (x2 - x1)**2)) / 2*math.sin((pi)/2)
        length = (dist*(pi)) / semiArcTime 
        return length 
    else 
        
    
def time(distance, speed):
    return distance/speed
    
    
def xdot(distance, time):
    return distance/time


def thetadot(radius, time):
    
    
def time(distance, speed):
    return distance/speed
    
    
def xdot(distance, time):
    return distance/time


def thetadot(radius, time):
    
    
def pd(xdot, thetadot):
    









# Start the program
print("Running FinalProjectV1.py")
#while(1):
print(getArray())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    time.sleep(0.2)

    
    