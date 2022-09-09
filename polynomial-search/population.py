#x^3+2y^2+6z+w = 10
import individual
import numpy as np
import random

CHROMOSOME_SIZE = 4
N_SURVIVORS = 3
N_CHILDREN = 6
FITNESS_GOAL = 10
N_MUTATIONS = 5

class Population:

    def __init__(self, population_size, population=[]):
        self.population_size = population_size
        self.population = population

    def initialize_population(self):
        for _ in range(self.population_size):
            genes = []
            for __ in range(CHROMOSOME_SIZE):
                gene = round(np.random.uniform(low=-5, high=5), 4)
                genes.append(gene)
            individual_x = individual.Individual(genes)
            self.population.append(individual_x)
        self.calculate_fitness()

    def get_population(self):
        return self.population

    def crossover(self):
        new_population = self.get_fittest_members() #top N solutions are hardcoded into the next population (eliteism)
        for _ in range(int(N_CHILDREN/2)):
            crossover_point = random.randint(1, CHROMOSOME_SIZE) #random crossover point in the chromosome
            parent1, parent2 = random.sample(range(0, N_SURVIVORS), 2) #Select two of the best parents to create a offspring with crossover
            child1_chromosome = self.get_fittest_members()[parent1].get_chromosome()[:crossover_point] + self.get_fittest_members()[parent2].get_chromosome()[crossover_point:] #Part of the chromosome from parent one combined with an fitting part from parent 2
            child2_chromosome = self.get_fittest_members()[parent2].get_chromosome()[:crossover_point] + self.get_fittest_members()[parent1].get_chromosome()[crossover_point:] 
            child1 = individual.Individual(child1_chromosome)
            child2 = individual.Individual(child2_chromosome)
            new_population.extend([child1, child2])
        self.population = new_population

    def mutation(self):
        for _ in range(random.randint(3, N_MUTATIONS)):
            mutated_individual_idx = random.randint(0, self.population_size - 1)
            mutated_gene_idx = random.randint(0, CHROMOSOME_SIZE - 1)
            gene_mutation = round(np.random.uniform(low=-4, high=-4), 4)

            self.get_population()[mutated_individual_idx].chromosome[mutated_gene_idx] += gene_mutation #edit_chromosome()
            self.get_population()[mutated_individual_idx].chromosome[mutated_gene_idx] = round(self.get_population()[mutated_individual_idx].chromosome[mutated_gene_idx], 4)
        self.calculate_fitness()

    def get_fittest_members(self):
        self.population = sorted(self.population, key=lambda x: x.get_fitness())
        return self.population[:N_SURVIVORS]

    def calculate_fitness(self): 
        for individual in self.get_population():
            individual.calculate_fitness(FITNESS_GOAL) #calculate how close each individuals solutions is to solving x

    def get_best_fitness(self):
        return self.get_fittest_members()[0].get_fitness()

