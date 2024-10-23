from Functions import Function, FunctionType
from SimulatedAnnealing import SimulatedAnnealing
from animation import run_animation


def main():
    function = Function(FunctionType.ACKLEY)
    simulatedAnnealing = SimulatedAnnealing(function=function, temperature=100, cooling_rate=0.99, cluster_scale=0.4)
    bestPoint, bestValue = simulatedAnnealing.search_min()

    function.show_plot(custom_point=bestPoint)

    run_animation(simulatedAnnealing.history, function)




if __name__ == '__main__':
    main()
