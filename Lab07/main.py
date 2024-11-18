from Functions import Function, FunctionType
from SomaAllToOne import SomaAllToOne
from animation import  run_animation
def main():

    function = Function(FunctionType.SCHWEFEL)

    soma = SomaAllToOne(population_size=100, function=function, PRT=0.5, path_length=1, step=0.1, m_max=100)

    best_solution, best_fitness = soma.search_min()

    function.show_plot(custom_point=best_solution)
    run_animation(soma.history, function)



if __name__ == '__main__':
    main()
