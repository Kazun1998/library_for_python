class Hash_Table:
    __slots__=("table", "seed")

    def __init__(self):
        from random import randint
        self.table={}
        self.seed=randint(-(1<<63)-1, (1<<63)-1)

    def get(self, key, default=None):
        return self.table.get(key^self.seed, default)

    def __len__(self):
        return len(self.table)

    def __getitem__(self, key):
        h=key^self.seed
        if h in self.table:
            return self.table[h]
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        self.table[key^self.seed]=value

    def __iter__(self):
        return self.keys()

    def __contains__(self, key):
        return key^self.seed in self.table

    def clear(self):
        self.table.clear()

    def keys(self):
        for alpha in self.table:
            yield alpha^self.seed

    def values(self):
        return self.table.values()

    def items(self):
        for alpha in self.table:
            yield (alpha^self.seed, self.table[alpha])

class Hash_Set:
    def __init__(self):
        from random import randint
        self.set=set()
        self.seed=randint(-(1<<63)-1, (1<<63)-1)

    def add(self, value):
        self.set.add(value^self.seed)

    def __contains__(self, value):
        return value^self.seed in self.set
