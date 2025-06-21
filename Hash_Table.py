from random import randint
from typing import TypeVar, Generic, Optional, Hashable

V = TypeVar('V')
class Hash_Table(Generic[V]):
    __slots__ = ("__table", "__seed")

    def __init__(self):
        self.__table: dict[Hashable, V] = {}
        self.__seed = randint(-(1 << 63) - 1, (1 << 63) - 1)

    @property
    def seed(self) -> int:
        return self.__seed

    def get(self, key: Hashable, default: V = None) -> Optional[V]:
        return self.__table.get(key^self.seed, default)

    def __len__(self) -> int:
        return len(self.__table)

    def __getitem__(self, key: Hashable) -> V:
        k = hash(key) ^ self.seed
        if k in self.__table:
            return self.__table[k]
        else:
            raise KeyError(key)

    def __setitem__(self, key: Hashable, value: V):
        self.__table[hash(key) ^ self.seed] = value

    def __iter__(self):
        return self.keys()

    def __contains__(self, key: Hashable) -> bool:
        return hash(key) ^ self.seed in self.__table

    def clear(self):
        self.__table.clear()

    def keys(self):
        for alpha in self.__table:
            yield alpha ^ self.seed

    def values(self):
        return self.__table.values()

    def items(self):
        for alpha in self.__table:
            yield (alpha ^ self.seed, self.__table[alpha])

class Hash_Set:
    def __init__(self):
        from random import randint
        self.set=set()
        self.seed=randint(-(1<<63)-1, (1<<63)-1)

    def add(self, value):
        self.set.add(value^self.seed)

    def __contains__(self, value):
        return value^self.seed in self.set
