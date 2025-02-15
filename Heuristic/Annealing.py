from random import random
from math import exp

class Annealing:
    def __init__(self, temperature: float, alpha: float, phase: int = 1) -> "Annealing":
        self.temperature = temperature
        self.alpha = alpha
        self.phase = phase
        self.count = 0

    def judge(self, before, after) -> bool:
        self.count += 1
        if self.count == self.phase:
            self.temperature *= self.alpha
            self.count = 0

        if after == before:
            return False

        if after > before:
            return True
        else:
            return random() < exp((after - before) / self.temperature)
