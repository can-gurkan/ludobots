import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
amplitudeBL = numpy.pi/4; frequencyBL = 20;  phaseOffsetBL = 0
amplitudeFL = numpy.pi/4; frequencyFL = 20;  phaseOffsetFL = numpy.pi/4
theta = numpy.linspace(0, 2*numpy.pi, 1000)
targetAnglesBL = amplitudeBL * numpy.sin(theta * frequencyBL + phaseOffsetBL)
targetAnglesFL = amplitudeFL * numpy.sin(theta * frequencyFL + phaseOffsetFL)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_BackLeg', controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesBL[i], maxForce=15)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_FrontLeg', controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesFL[i], maxForce=15)
    time.sleep(1./500)
    print(i)
p.disconnect()

numpy.save('data/BackLegSensorData.npy',backLegSensorValues)
numpy.save('data/FrontLegSensorData.npy',frontLegSensorValues)
#print(backLegSensorValues)

