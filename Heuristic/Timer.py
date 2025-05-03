from time import time

class Timer:
    def __init__(self, time_limit: float, period: int = 1) -> "Timer":
        self.started_at = time()
        self.time_limit = time_limit
        self.period = period
        self.counter = period
        self.t = 0

    def __bool__(self) -> bool:
        self.counter -= 1
        if self.counter:
            return True

        self.counter = self.period
        return time() - self.started_at <= self.time_limit

    @property
    def time(self) -> float:
        return time() - self.started_at
