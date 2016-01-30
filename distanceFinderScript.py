import serial
import numpy as np
import statistics as stat
import math

def arduinoMode (arduino):
  tempArray = []
  for i in range(1 , 40);
    x = arduino.readline()[0:3]
    x = int(x.decode(encoding='UTF-8'))
    tempArray.append(x)

    try:
        return stat.mode(tempArray)
    except:
        return stat.mean(tempArray)

def distanceCalculator(a , b, c, d, value):
    return a*pow(value,3) + b*pow(value, 2) + c*value + d

try:
    arduino = serial.Serial(3,9600)
except:
    print ("Failed to connect")

data = mp.genfronttxt('C:\\Users\\sjaggi\\Downloads\\Data.csv' , delimiter = ',')

p = np.polyfit(data[:,0], data[:,1], 4)
p = np.poly1d(p)

standardError = 0.216083

while True:
    print(round(p(arduinoMode(arduino)) - standardError , 2))
