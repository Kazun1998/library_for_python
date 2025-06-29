from typing import TypeVar, Generic, Callable
from heapq import heappush, heappop

OrderedGroup = TypeVar('OrderedGroup')
class Best_Sum(Generic[OrderedGroup]):
    def __init__(self, K: int, add: Callable[[OrderedGroup, OrderedGroup], OrderedGroup], neg: Callable[[OrderedGroup], OrderedGroup], zero: OrderedGroup, reversal: bool = False):

        self.K = max(0, K)
        self.__reversal = reversal

        self.more: list[OrderedGroup] = []
        self.more_count: dict[OrderedGroup, int] = {}
        self.more_sum = zero
        self.more_length = 0

        self.less: list[OrderedGroup] = []
        self.less_count: dict[OrderedGroup, int] = {}
        self.less_sum = zero
        self.less_length  = 0

        self.__add = add
        self.__neg = neg
        self.__sub: Callable[[OrderedGroup, OrderedGroup], OrderedGroup] = lambda x, y: add(x, neg(y))

    @property
    def reversal(self) -> int:
        return self.__reversal

    def _more_insert(self, x: OrderedGroup):
        self.more_sum = self.__add(self.more_sum, x)
        self.more_length += 1

        if x in self.more_count:
            self.more_count[x] += 1
        else:
            self.more_count[x] = 1
            heappush(self.more, x)

    def _less_insert(self, x: OrderedGroup):
        self.less_sum = self.__add(self.less_sum, x)
        self.less_length += 1

        if x in self.less_count:
            self.less_count[x] += 1
        else:
            self.less_count[x] = 1
            heappush(self.less, -x)

    def _more_discard(self, x: OrderedGroup):
        self.more_sum = self.__sub(self.more_sum, x)
        self.more_length -= 1
        self.more_count[x] -= 1

        if self.more_count[x] == 0:
            del self.more_count[x]

        while self.more and (self.more[0] not in self.more_count):
            heappop(self.more)

    def _less_discard(self, x: OrderedGroup):
        self.less_sum = self.__sub(self.less_sum, x)
        self.less_length -= 1
        self.less_count[x] -= 1

        if self.less_count[x] == 0:
            del self.less_count[x]

        while self.less and (-self.less[0] not in self.less_count):
            heappop(self.less)

    def _more_to_less(self):
        x = self.more[0]
        self._more_discard(x)
        self._less_insert(x)

    def _less_to_more(self):
        x = -self.less[0]
        self._less_discard(x)
        self._more_insert(x)

    def _validation(self):
        if self.more_length > self.K:
            while self.more_length > self.K:
                self._more_to_less()
        elif self.more_length < self.K:
            while self.less_length > 0 and self.more_length < self.K:
                self._less_to_more()

    def __len__(self) -> int:
        return self.more_length + self.less_length

    def __contains__(self, value: OrderedGroup) -> bool:
        return (value in self.more_count) or (value in self.less_count)

    def count(self, value: OrderedGroup) -> int:
        return self.more_count(value, 0) + self.less_count(value, 0)

    def insert(self, x: OrderedGroup):
        if self.reversal:
            x = self.__neg(x)

        self._more_insert(x)
        self._validation()

    def discard(self, x: OrderedGroup):
        if self.reversal:
            x = self.__neg(x)

        if x not in self:
            return

        if x >= self.more[0]:
            self._more_discard(x)
        else:
            self._less_discard(x)
        self._validation()

    def best_sum(self) -> OrderedGroup:
        assert not self.reversal
        return self.more_sum

    def worst_sum(self) -> OrderedGroup:
        assert self.reversal
        return self.__neg(self.more_sum)

    def all_sum(self) -> OrderedGroup:
        return self.sign * self.__add(self.more_sum, self.less_sum)

    def change_K(self, K: int):
        self.K = max(0, K)
        self._validation()

class Worst_Sum(Best_Sum[OrderedGroup]):
    def __init__(self, K: int, add: Callable[[OrderedGroup, OrderedGroup], OrderedGroup], neg: Callable[[OrderedGroup], OrderedGroup], zero: OrderedGroup, reversal: bool = False):
        Best_Sum.__init__(self, K, add, neg, zero, not reversal)
