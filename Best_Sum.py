from heapq import heappush, heappop

class Best_Sum:
    def __init__(self, K, reversal = 1):

        self.K = max(0, K)
        self.reversal = reversal

        self.more = []
        self.more_count = {}
        self.more_sum = 0
        self.more_length = 0

        self.less = []
        self.less_count = {}
        self.less_sum = 0
        self.less_length  = 0

    def _more_insert(self, x):
        self.more_sum += x
        self.more_length += 1

        if x in self.more_count:
            self.more_count[x] += 1
        else:
            self.more_count[x] = 1
            heappush(self.more, x)

    def _less_insert(self, x):
        self.less_sum += x
        self.less_length += 1

        if x in self.less_count:
            self.less_count[x] += 1
        else:
            self.less_count[x] = 1
            heappush(self.less, -x)

    def _more_discard(self, x):
        self.more_sum -= x
        self.more_length -= 1
        self.more_count[x] -= 1

        if self.more_count[x] == 0:
            del self.more_count[x]

        while self.more and (self.more[0] not in self.more_count):
            heappop(self.more)

    def _less_discard(self, x):
        self.less_sum -= x
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

    def __len__(self):
        return self.more_length + self.less_length

    def __contains__(self, value):
        return (value in self.more_count) or (value in self.less_count)

    def count(self, value):
        return self.more_count(value, 0) + self.less_count(value, 0)

    def insert(self, x):
        x *= self.reversal
        self._more_insert(x)
        self._validation()

    def discard(self, x):
        x *= self.reversal

        if x not in self:
            return

        if x >= self.more[0]:
            self._more_discard(x)
        else:
            self._less_discard(x)
        self._validation()

    def best_sum(self):
        assert self.reversal == 1
        return self.more_sum

    def worst_sum(self):
        assert self.reversal == -1
        return -self.more_sum

    def all_sum(self):
        return self.reversal * (self.more_sum + self.less_sum)

    def change_K(self, K):
        self.K = max(0, K)
        self._validation()

class Worst_Sum(Best_Sum):
    def __init__(self, K, reversal = 1):
        Best_Sum.__init__(self, K, - reversal)
