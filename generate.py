import pyrosim.pyrosim as pyrosim

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
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[width, length, height])
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position=[0, 0, 0.5])
    pyrosim.Send_Cube(name="Leg", pos=[0, 0, 1], size=[width, length, height])
    pyrosim.End()


if __name__ == "__main__":
    Create_World()
    Create_Robot()
