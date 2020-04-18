#FinalProjectV1.py
# Code purpose: Do interesting things of little importance
# Import external libraries
import numpy as np
import time as t
import math
pi = 3.14159265359
# Import internal programs
# import L2_vector.py as vector
# import L2_log as log
import L2_inverse_kinematics as invkin
# import L2_kinematics.py as kin
#import L1_lidar as lidar
import L2_speed_control as sc
import csv

#takes path data from external csv file and returns populated array
#returns [x global, y global, speed setting, circle radius] 
#A positive radius curves to the left and a negative curves to the right
#Speed settings are 1 through 5, 5 beaing the fastest.
pathdata = np.genfromtxt('PathData.csv', delimiter=',')



def distance(stepnum):
	x1=pathdata[stepnum][0]
	y1=pathdata[stepnum][1]
	x2=pathdata[stepnum+1][0]
	y2=pathdata[stepnum+1][1]
	theta=pathdata[stepnum][3]

	if theta == 0:                                                                  # calculation for a straight line
		dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
		length = dist
		return length

	elif abs(theta) == 1.57:                                                           # quarter circle (might need | -pi/2)
		dist = (math.sqrt((y2 - y1)**2 + (x2 - x1)**2)) / 2*math.sin((pi/2)/2)
		length = dist * abs(pi/2)
		return length 

	elif abs(theta) == 3.14:                                                             # semi circle
		dist = (math.sqrt((y2 - y1)**2 + (x2 - x1)**2)) / 2*math.sin((pi)/2)
		length = dist * abs(pi) 
		return length 


def xdotthetadot(stepnum):
	theta=pathdata[stepnum][3]
	speed=pathdata[stepnum][2]
	print(distance(stepnum))
	time=distance(stepnum)/.4
	xdot=.4/(6-speed)
	thetadot=(theta/time)/(6-speed)
	print(theta,"/",time,"/",speed,"=",thetadot)
	return np.array([xdot,thetadot])

def time(stepnum):
	return distance(stepnum)/.4

def step(stepnum):
	myPhiDots=invkin.convert(xdotthetadot(stepnum))
	sc.driveOpenLoop(myPhiDots)
	
def drive():
	for num in range(13):
		start=t.time()
		timeDifference=t.time()-start
		duration=time(num)
		while timeDifference<duration:
			timeDifference=t.time()-start
			print(num)
			step(num)
		
		
	print("Thats all folks")
	
# Start the program
print("Running FinalProjectV1.py")
drive()
