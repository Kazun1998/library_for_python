class Unique_Counter:
    def __init__(self):
        self.list = []

    def add(self, x):
        self.list.append(x)

    def count(self):
        if not self.list:
            return 0

        self.list.sort()
        res = 1
        for i in range(1, len(self.list)):
            if self.list[i] != self.list[i - 1]:
                res += 1
        return res
