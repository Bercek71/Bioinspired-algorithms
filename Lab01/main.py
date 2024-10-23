from Functions import Function, FunctionType
from BlindSearch import BlindSearch
from animation import run_animation

def main():
    function = Function(FunctionType.ACKLEY)
    # blind_search = BlindSearch(function, iterations=50)
    # blind_search.search_min()
    # blind_search.visualize_solution()
    # run_animation(blind_search.history, function)

    function.show_plot()
    function = Function(FunctionType.SPHERE)
    function.show_plot()
    function = Function(FunctionType.GRIEWANK)
    function.show_plot()
    function = Function(FunctionType.ROSENBROCK)
    function.show_plot()
    function = Function(FunctionType.LEVY)
    function.show_plot()
    function = Function(FunctionType.ZAKHAROV)
    function.show_plot()
    function = Function(FunctionType.RASTRIGIN)
    function.show_plot()
    function = Function(FunctionType.MICHALEWICZ)
    function.show_plot()
    function = Function(FunctionType.SCHWEFEL)
    function.show_plot()


if __name__ == '__main__':
    main()
