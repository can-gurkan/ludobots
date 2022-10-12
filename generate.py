import pyrosim.pyrosim as pyrosim

length = 1; width = 1; height = 1
x = 0; y = 0; z = height/2.

pyrosim.Start_SDF("boxes_tower.sdf")
for i in range(10):
    if i != 0:
        z = z + height
        length *= .9; width *= .9; height *= .9
    pyrosim.Send_Cube(name="Box"+str(i), pos=[x, y, z], size=[width, length, height])
pyrosim.End()

