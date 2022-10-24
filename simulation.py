import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self,directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravityConst)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.simLength):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(c.sleepTime)
            #print(i)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()