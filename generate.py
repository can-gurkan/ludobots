import pyrosim.pyrosim as pyrosim

length = 1; width = 1; height = 1
x = 0; y = 0; z = height

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z/2.] , size=[width,length,height])
pyrosim.Send_Cube(name="Box2", pos=[x+width,y,z/2.+height] , size=[width,length,height])
pyrosim.End()

