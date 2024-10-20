from Functions import Function, FunctionType
from SimulatedAnnealing import SimulatedAnnealing
from animation import run_animation


def main():
    function = Function(FunctionType.ACKLEY)
    # hillClimbing = HillClimbing(function=function, dimension=2, cluster_scale=0.4)
    #
    # bestPoint = hillClimbing.search_min()
    #
    # function.show_plot(custom_point=bestPoint)
    #
    # run_animation(hillClimbing.history, function)

    # Simulated Annealing
    simulatedAnnealing = SimulatedAnnealing(function=function, temperature=100, cooling_rate=0.99, cluster_scale=0.4)
    bestPoint, bestValue = simulatedAnnealing.search_min()

    function.show_plot(custom_point=bestPoint)

    run_animation(simulatedAnnealing.history, function)




if __name__ == '__main__':
    main()
