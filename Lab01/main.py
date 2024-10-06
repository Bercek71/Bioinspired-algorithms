from Functions import Function, FunctionType
from BlindSearch import BlindSearch
from animation import run_animation

def main():
    function = Function(FunctionType.RASTRIGIN)
    blind_search = BlindSearch(function, iterations=100)
    blind_search.search_min()
    blind_search.visualize_solution()
    run_animation(blind_search.history, function)


if __name__ == '__main__':
    main()
