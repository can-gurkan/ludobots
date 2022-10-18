from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate('DIRECT')
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        print(self.parent.fitness,self.child.fitness)
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        #print(self.parent.fitness)
        #print(self.child.fitness)
        if self.child.fitness >= self.parent.fitness:
            self.parent = self.child
            self.parent.Create_Brain()

    def Show_Best(self):
        print('pf=',self.parent.fitness)
        self.parent.Create_Brain()
        self.parent.Evaluate('GUI')
        