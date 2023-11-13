import random
import classes
import solver
import matplotlib.pyplot as plt

def optimize(task):
    pop_init = create_initial_population(task) #[v1, v2, v3]
    population = pop_init
    #print([i.stress for i in population])
    CM_init = classes.Vector([sum([population[i].variables[0] / population[i].stress for i in
                              range(0, len(population))]) / sum(
        [1 / population[i].stress for i in range(0, len(population))]),
                         sum([population[i].variables[1] / population[i].stress for i in
                              range(0, len(population))]) / sum(
                             [1 / population[i].stress for i in range(0, len(population))])])
    pop_new = []
    i = 0
    convergence = 10
    solver.solve([CM_init],task)
    result = [CM_init.stress]
    print(CM_init.stress)
    plt.figure()
    while convergence > 1 and i < 20:
        i+=1
        pop_ch,CM = create_new_population(pop_init, task,i)
        #pop_init = selection(pop_ch + pop_init)
        result.append(CM.stress)
        convergence = abs(result[i] - result[i-1])
        print('convergence = ',convergence)
        #print(result)
        #print([n for n in range(0,i+1)])
        print(result)
        plt.plot([n for n in range(0,i+1)],result)
        plt.xlabel('Iteration')
        plt.ylabel('Stress Pa')
    plt.show()
    print('end')
    print('==========Parameters=========')
    print(' r1 = ',CM.variables[0],' r2 = ',CM.variables[1])
    return pop_init[0]


def create_initial_population(task):
    population = []
    for i in range(int(task.population_size)):
        population.append(classes.Vector([random.uniform(0.0000001, float(task.diametr_restr)),
                                          random.uniform(0.0000001, float(task.diametr_restr))]))
    solver.solve(population, task)
    return population

def create_new_population(pop_init, task,iteration):
    population = pop_init
    CM = classes.Vector([sum([population[i].variables[0]/population[i].stress for i in range(0,len(population))])/sum([1/population[i].stress for i in range(0,len(population))]),
                         sum([population[i].variables[1]/population[i].stress for i in range(0,len(population))])/sum([1/population[i].stress for i in range(0,len(population))])])
    pop_new = []
    for i in range(int(task.population_size)):
        pop_new.append(classes.Vector([CM.variables[0] + random.uniform(0.0000001, float(task.diametr_restr))/iteration*task.diametr_restr,
                                          CM.variables[1] + random.uniform(0.0000001, float(task.diametr_restr))/iteration*task.diametr_restr]))
    solver.solve(pop_new, task)
    population = pop_new
    CM_New = classes.Vector([sum([population[i].variables[0] / population[i].stress for i in
                              range(0, len(population))]) / sum(
        [1 / population[i].stress for i in range(0, len(population))]),
                         sum([population[i].variables[1] / population[i].stress for i in
                              range(0, len(population))]) / sum(
                             [1 / population[i].stress for i in range(0, len(population))])])
    pop_new = []
    CMP = [CM_New]

    solver.solve(CMP,task)
    return pop_new,CM_New





