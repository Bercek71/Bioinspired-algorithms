from Functions import Function, FunctionType
from ParticleSwarm import ParticleSwarm
from animation import  run_animation
def main():

    function = Function(FunctionType.ACKLEY)

    pso = ParticleSwarm(function, 1000, 10000, 0.1, 0.4, 0.1)

    result = pso.search_min()


    function.show_plot(custom_point=result.best_position)
    run_animation(pso.history, function)



if __name__ == '__main__':
    main()
