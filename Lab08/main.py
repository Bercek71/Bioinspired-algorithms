from AntColony import AntColony
from GeneticAlgorithm import GeneticAlgorithm
from TravellingSalesmanProblem import TravellingSalesmanProblem
from animation import run_animation
import time

def main():

    tsp = TravellingSalesmanProblem(35)

    antColone = AntColony()


    start = time.time()
    best_route, best_distance = antColone.solve(tsp, 100, 100)
    end = time.time()
    print(f"Time: {end - start}")
    print(best_route)
    print(best_distance)
    tsp.setRoutes(best_route)

    tsp.show()

    run_animation(antColone.history, tsp.cities)

if __name__ == '__main__':
    main()
