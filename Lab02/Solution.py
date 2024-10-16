from Functions import Function

class Solution:
    def __init__(self, function: Function, dimension, lower_bound, upper_bound):
        self.function = function
        self.dimension = dimension
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def search(self):
        raise NotImplementedError

    def visualize_solution(self):
        raise NotImplementedError