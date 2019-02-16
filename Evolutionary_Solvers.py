from Function import MultivariateFunction
import random, math
import numpy as np

class EvolutionarySolver:
    def __init__(self):
        pass

    def GeneratePopulation(self, pop_size, num_var, lower, upper):
        population = []
        gene = []
        for i in range(pop_size):
            for j in range(num_var):
                gene.append(random.randint(lower, upper))
            population.append(gene)
            gene = []
        return population

    def Breed(self, population, mutation_percent, k, f):
        fitnesses = [self.Fitness(gene, f) for gene in population]
        fitnesses = sorted(enumerate(fitnesses), key=lambda x:x[1])
        scores = [population[i] for i in range(len(population))]

        topk = scores[:2*k]

        ''' Top-k Crossover '''

        new_pop = list()
        for i in range(k // 2):
            mate1 = topk[i]
            mate2 = random.choice(topk[i:len(topk)])
            if random.randint(0, 100) >= mutation_percent:
                mutate = True
            else:
                mutate = False
            child = self.Crossover(mate1, mate2, mutate=mutate)
            new_pop += [child]
        return new_pop


    def Crossover(self, mate1, mate2, mutate=True):
        if mutate:
            return [(mate1[0] + mate2[0]) / 2 + random.uniform(-1.0, 1.0),
                (mate1[1] + mate2[1]) / 2 + random.uniform(-1.0, 1.0),
                (mate1[2] + mate2[2]) / 2 + random.uniform(-1.0, 1.0),
                (mate1[3] + mate2[3]) / 2 + random.uniform(-1.0, 1.0)]
        return [(mate1[0] + mate2[0]) / 2,
                (mate1[1] + mate2[1]) / 2,
                (mate1[2] + mate2[2]) / 2,
                (mate1[3] + mate2[3]) / 2]

    def Fitness(self, gene, f):
        return abs(f(gene))
    
    def __call__(self, f, num_var, lower, upper, pop_size, mutation_percent, k):
        thres = 1e-3
        solved = False

        pop = self.GeneratePopulation(pop_size, num_var, lower, upper)

        i = 0
        while not solved:
            fitnesses = [self.Fitness(gene, f) for gene in pop]
            best_fit = min(fitnesses)
            if min(fitnesses) <= thres:
                ind = fitnesses.index(min(fitnesses))
                best_gene = pop[ind]
                solved = True
            else:
                pop = self.Breed(pop, mutation_percent, k, f)
                pop += self.GeneratePopulation(pop_size - len(pop), num_var, lower, upper)
            print("Generation: {}, best_fit: {}".format(i, best_fit))
            i += 1
        return best_gene

if __name__ == "__main__":
    f1 = MultivariateFunction("x**2 + 2*y + z - u*0.2 - 3")
    evo_sol = EvolutionarySolver()

    solution = evo_sol(f1, 4, -1000, 1000, 500, 5, 50)
    print("Solution found: ", solution, "Fitness: ", f1(solution))