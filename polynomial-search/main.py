import population

population1 = population.Population(9)
population1.initialize_population()

counter = 1
for x in range(100):
    population1.crossover()
    population1.mutation()
    print(f'Iteration {counter}: Best fitness: {population1.get_best_fitness()}')
    #if(population1.get_best_fitness() < 0.01):
     #   break
    # counter += 1
    # for indv in population1.get_population():
    #     print(indv.chromosome)
    # print()

print(population1.get_best_fitness())