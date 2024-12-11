from Functions import Function, FunctionType
from animation import  run_animation
from TeachingLearningBasedOptimization import TeachingLearningBasedOptimization


def main():

    function = Function(FunctionType.ACKLEY)

    tlbo  = TeachingLearningBasedOptimization(population_size=100, dimension=2, iterations=100, function=function)

    best_solution, best_fitness = tlbo.search_min()
    print(f"Best solution: {best_solution}, Best fitness: {best_fitness}")
    function.show_plot(custom_point=best_solution)
    run_animation(tlbo.history, function)



if __name__ == '__main__':
    main()
