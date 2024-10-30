from GeneticAlgorithm import GeneticAlgorithm
from TravellingSalesmanProblem import TravellingSalesmanProblem
from animation import run_animation
import time

def main():

    tsp = TravellingSalesmanProblem(35)

    genAlg = GeneticAlgorithm(100, 1000)
    start = time.time()
    best_route, best_distance = genAlg.solve(tsp)
    end = time.time()
    print(f"Time: {end - start}")
    print(best_route)
    print(best_distance)
    tsp.setRoutes(best_route)

    tsp.show()

    run_animation(best_route, tsp.cities)

if __name__ == '__main__':
    main()
