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
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_BackLeg', controlMode=p.POSITION_CONTROL, targetPosition=random.uniform(-numpy.pi/2,numpy.pi/2), maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName='Torso_FrontLeg', controlMode=p.POSITION_CONTROL, targetPosition=random.uniform(-numpy.pi/2,numpy.pi/2), maxForce=50)
    time.sleep(1./500)
    print(i)
p.disconnect()

numpy.save('data/BackLegSensorData.npy',backLegSensorValues)
numpy.save('data/FrontLegSensorData.npy',frontLegSensorValues)
#print(backLegSensorValues)

