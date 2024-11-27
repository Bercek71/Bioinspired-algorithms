## Particle Swarm algorithm Optimization with inertia weight
from Functions import Function
import numpy as np
import random

class ParticleSwarm:
    def __init__(self, function: Function, swarm_size, max_iter, w, c1, c2 ):
        self.function = function
        self.swarm_size = swarm_size
        self.max_iter = max_iter
        self.lower_bound = function.lower_bound
        self.upper_bound = function.upper_bound
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.history = []

    class Particle:
        def __init__(self, lower_bound, upper_bound, dimension=2):
            self.position = np.random.uniform(low=lower_bound, high=upper_bound, size=dimension)
            self.velocity = np.random.uniform(low=-1, high=1, size=dimension)
            self.best_position = self.position
            self.best_evaluation = float('inf')
            self.evaluation = float('inf')
            self.lower_bound = lower_bound
            self.upper_bound = upper_bound


        def _update_velocity(self, gbest, w, c1, c2):
            inertia = w * self.velocity
            cognitive = c1 * random.random() * (self.best_position - self.position)
            social = c2 * random.random() * (gbest.best_position - self.position)
            self.velocity = inertia + cognitive + social

        def _update_position(self):
            # write in np
            self.position = self.position + self.velocity
            self.position = np.clip(self.position, self.lower_bound, self.upper_bound)


        def _evaluate(self, function):
            self.evaluation = function.evaluate(self.position)
            if self.evaluation < self.best_evaluation:
                self.best_evaluation = self.evaluation
                self.best_position = self.position

        def update(self, gbest, w, c1, c2, function):
            self._update_velocity(gbest, w, c1, c2)
            self._update_position()
            self._evaluate(function)

    def _initialize_swarm(self):
        return [self.Particle(self.lower_bound, self.upper_bound) for _ in range(self.swarm_size)]

    def _get_best_particle(self, swarm):
        return min(swarm, key=lambda x: x.best_evaluation)


    def print_progress(self, gbest, i):
        percentage = (i + 1) / self.max_iter * 100

        max_symbols = 40

        print(f"\r|{int(percentage / 2) * '#'}{int((100 - percentage) / 2) * '-'}|\t[{percentage: .2f}%]\t\tBest evaluation: {gbest.best_evaluation: .4f}",
                end="", flush=True)

    def search_min(self, verbose=True):
        swarm = self._initialize_swarm()
        gbest = self._get_best_particle(swarm)
        if verbose:
            print(f"|\tFunction\t|\t{self.function.name}\t|")

        for i in range(self.max_iter):
            if verbose:
                self.print_progress(gbest, i)
            for particle in swarm:
                particle.update(gbest, self.w, self.c1, self.c2, self.function)
                if particle.evaluation < gbest.evaluation:
                    gbest = particle
            self.history.append((gbest.position, gbest.evaluation))
        if verbose:
            print("\n-------------------------------------------------")
            print(f"Best position: {gbest.best_position}")
            print(f"Best evaluation: {gbest.best_evaluation}")

        return gbest