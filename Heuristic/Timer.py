from time import time

class Timer:
    def __init__(self, time_limit: float, period: int = 1) -> "Timer":
        self.__started_at = time()
        self.__time_limit = time_limit
        self.__period = period
        self.__counter = period

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(time_limit={self.time_limit}, self.period={self.period})"

    def __bool__(self) -> bool:
        self.__counter -= 1
        if self.__counter:
            return True

        self.__counter = self.period
        return time() - self.started_at <= self.time_limit

    @property
    def started_at(self) -> float:
        return self.__started_at

    @property
    def period(self) -> int:
        return self.__period

    @property
    def time_limit(self) -> float:
        return self.__time_limit

    @property
    def time(self) -> float:
        """ 経過時間を出力する.

        Returns:
            float: 経過時間
        """

        return time() - self.started_at
