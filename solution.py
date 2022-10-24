import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:

    def __init__(self,id):
        self.myID = id
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()

    def Set_ID(self,id):
        self.myID = id

    def Start_Simulation(self,directOrGUI):
        os.system("python3 simulate.py " + str(directOrGUI) + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while (not os.path.exists("fitness"+str(self.myID)+".txt")):
            time.sleep(0.01)
        f = open("fitness"+str(self.myID)+".txt", "r")
        fitness = f.read()
        if fitness != "":
            self.fitness = float(fitness)
        else:
            #print("fitness" + str(self.myID) + ".txt")
            time.sleep(0.05)
            fitness = f.read()
            self.fitness = float(fitness)
        f.close()
        os.system("rm " + "fitness"+str(self.myID)+".txt")

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1.
        self.Create_Brain()

    def Create_World(self):
        length = 1;
        width = 1;
        height = 1
        x = -2;
        y = 2;
        z = height / 2.
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[width, length, height])
        pyrosim.End()

    def Create_Robot(self):
        length = 1;
        width = 1;
        height = 1
        x = 0;
        y = 0;
        z = height / 2.
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[x, y, 1.5], size=[width, length, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[width, length, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[width, length, height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
