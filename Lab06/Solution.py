from Functions import Function

class Solution:
    def __init__(self, x, evaluation):
        self.x = x
        self.evaluation = evaluation

    def __str__(self):
        return f"x = {self.x}, f(x): {self.evaluation}"