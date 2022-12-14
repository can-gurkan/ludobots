import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    length = 1; width = 1; height = 1
    x = -2; y = 2; z = height / 2.
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[width, length, height])
    pyrosim.End()

def Create_Robot():
    length = 1; width = 1; height = 1
    x = 0; y = 0; z = height / 2.
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, 1.5], size=[width, length, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[width, length, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[width, length, height])
    pyrosim.End()

def Create_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    for i in range(3):
        for j in range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1,1))
    pyrosim.End()


if __name__ == "__main__":
    Create_World()
    Create_Robot()
    Create_Brain()
