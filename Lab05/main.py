from Functions import Function, FunctionType
from DifferentialEvolution import DifferentialEvolution
from animation import run_animation


def main():
    function = Function(FunctionType.ROSENBROCK)

    differentialEvolution = DifferentialEvolution(number_of_individuals=10, generation_cycles=1000, dimension=2)

    bestPoint, bestValue = differentialEvolution.search(function)
    print(differentialEvolution.history)
    print(f"Best point: {bestPoint}")
    print(f"Best value: {bestValue}")
    function.show_plot(custom_point=bestPoint)

    run_animation(differentialEvolution.history, function)




if __name__ == '__main__':
    main()
