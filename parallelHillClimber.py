from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = dict()
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evaluate(self,solutions):
        for i in solutions.keys():
            solutions[i].Start_Simulation('DIRECT')
        for j in solutions.keys():
            solutions[j].Wait_For_Simulation_To_End()

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self,currGen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print(currGen)
        self.Select()

    def Spawn(self):
        self.children = dict()
        for k in self.parents.keys():
            self.children[k] = copy.deepcopy(self.parents[k])
            self.children[k].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for k in self.children.keys():
            self.children[k].Mutate()

    def Select(self):
        for k in self.parents.keys():
            if self.children[k].fitness >= self.parents[k].fitness:
                self.parents[k] = self.children[k]
                self.parents[k].Create_Brain()

    def Show_Best(self):
        bestKey, bestSol = max(self.parents.items(), key=lambda x: x[1].fitness)
        print('Best Fitness = ', bestSol.fitness)
        bestSol.Create_Brain()
        bestSol.Start_Simulation('GUI')

    def Print(self,currGen):
        print("Generation: " + str(currGen))
        print("Best Fitness: "+str(max([p.fitness for p in self.parents.values()])))
        print()
