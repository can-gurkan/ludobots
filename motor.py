import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.amplitude = c.amplitudeBL
        self.frequency = c.frequencyBL
        if self.jointName == "Torso_BackLeg":
            self.frequency /= 2
        self.offset = c.phaseOffsetBL
        theta = numpy.linspace(0, 2 * numpy.pi, c.simLength)
        self.motorValues = self.amplitude * numpy.sin(theta * self.frequency + self.offset)

    def Set_Value(self,t,robotId):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=self.motorValues[t], maxForce=c.maxForceBL)

    def Save_Values(self):
        numpy.save('data/'+str(self.jointName),self.motorValues)
