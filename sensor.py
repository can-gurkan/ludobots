import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.simLength)

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.simLength - 1:
            pass #print(self.values)

    def Save_Values(self):
        numpy.save('data/'+str(self.linkName),self.values)
