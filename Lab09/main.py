from Functions import Function, FunctionType
from animation import  run_animation
from FireflyAlgorithm import FireflyAlgorithm

def main():

    function = Function(FunctionType.ACKLEY)

    fireFly = FireflyAlgorithm(population_size=100, function=function, m_max=100, t=0.1, dimension=2, alpha=0.5, beta_0=1.0, gamma=1.0)

    best_solution, best_fitness = fireFly.search_min()

    function.show_plot(custom_point=best_solution)
    run_animation(fireFly.history, function)



if __name__ == '__main__':
    main()
