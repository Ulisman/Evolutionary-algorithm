class Individual:

    def __init__(self, chromosome=[]):
        self.chromosome = chromosome
        self.fitness = 0
    
    def get_fitness(self):
        return self.fitness
    
    def get_chromosome(self):
        return self.chromosome

    def add_gene(self, gene):
        self.chromosome.append(gene)

    def calculate_fitness(self, y):
        a, b, c, d = self.chromosome[0], self.chromosome[1], self.chromosome[2], self.chromosome[3]
        pred = a**3 + 2*b**2 + 6*c + d
        self.fitness = self.mean_squared_err(y, pred)

    def mean_squared_err(self, y, y_hat):
        mse = (y - y_hat) ** 2
        return mse
