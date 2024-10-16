from Functions import Function, FunctionType
from HillClimbing import HillClimbing
from animation import run_animation


def main():
    function = Function(FunctionType.SPHERE)
    hillClimbing = HillClimbing(function=function, dimension=2, cluster_scale=0.4)

    bestPoint = hillClimbing.search_max()

    function.show_plot(custom_point=bestPoint)

    run_animation(hillClimbing.history, function)


if __name__ == '__main__':
    main()
