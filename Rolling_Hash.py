from typing import TypeVar, Generic, Iterable, Callable

T = TypeVar('T')
class Rolling_Hash(Generic[T]):
    def __init__(self, S: Iterable[T], base: int, mod: int, hash_function: Callable[[T], int] = None):
        """ 列 S に対する Rolling Hash を生成する.

        Args:
            S (Iterable[T]): T の列
            base (int): Rolling Hashの元となる底
            mod (int): Rolling Hash の剰余
            hash_function (Callable[[T], int] | None, optional): 各 x in T におけるハッシュ値. None のときは恒等関数になる. Defaults to None.
        """

        self.mod = mod
        self.base = base
        self.length = len(S)
        self.power = power = [1]*(len(S)+1)
        self.hash_function = hash_function = hash_function if hash_function is not None else lambda x: x

        length = len(S)
        self.hash = h = [0] * (length + 1)

        for i in range(length):
            h[i + 1] = (base * h[i] + hash_function(S[i])) % mod

        for i in range(length):
            power[i + 1] = base * power[i] % mod

    def __hasher(self, X: Iterable[T]) -> int:
        assert len(X)<=len(self)
        h=0
        for i in range(len(X)):
            h = (h * self.base + self.hash_function(X[i])) % self.mod
        return h

    def get(self, l: int, r: int) -> int:
        """ 連続部分列 [l, r) に関するハッシュ値を求める.

        Args:
            l (int): 左端 (閉区間)
            r (int): 右端 (開区間)

        Returns:
            int: ハッシュ値
        """
        return (self.hash[r] - self.hash[l] * self.power[r - l]) % self.mod

    def count(self, T: int, start: int = 0) -> int:
        alpha = self.__hasher(T)
        return len([i for i in range(start, len(self) - len(T) + 1) if self[i: i + len(T)] == alpha])

    def find(self, T: Iterable[T], start: int = 0) -> int:
        alpha = self.__hasher(T)

        for i in range(start, len(self) - len(T) + 1):
            if alpha == self[i: i + len(T)]:
                return i
        return -1

    def rfind(self, T: Iterable[T], start: int = 0) -> int:
        alpha = self.__hasher(T)

        for i in range(len(self) - len(T), start - 1, -1):
            if alpha == self[i: i + len(T)]:
                return i
        return -1

    def index(self, T: Iterable[T], start: int = 0) -> int:
        ind = self.find(T, start)
        if ind == -1:
            raise ValueError("substring not found")
        return ind

    def __getitem__(self, index):
        if index.__class__==int:
            if index<0:
                index+=self.length
            assert 0<=index<self.length
            return self.get(index, index+1)
        elif index.__class__==slice:
            assert (index.step==None) or (index.step==1)
            L=index.start if index.start else 0
            R=index.stop if index.stop else len(self)
            if L<0:
                L+=len(self)
            if R<0:
                R+=len(self)
            return self.get(L,R)

    def __len__(self) -> int:
        return self.length

    def docking(self, l0: int, r0: int, l1: int, r1: int) -> int:
        """ [l0, r0) と [l1, r1) の部分列をドッキングしたハッシュを返す.
        """

        h0=self.get(l0,r0); h1=self.get(l1,r1)
        return (h0*self.power[r1-l1]+h1)%self.mod

#=================================================
class Double_Rolling_Hash(Generic[T]):
    def __init__(self, S: Iterable[T], base: int, mod0: int, mod1: int, hash_function: Callable[[T], int] = None):
        self.__length=len(S)
        self.__base=base
        self.__mod0=mod0
        self.__mod1=mod1
        self.hash_function = hash_function

        self.rh0=Rolling_Hash[T](S, base, mod0, hash_function)
        self.rh1=Rolling_Hash[T](S, base, mod1, hash_function)

    def encode(self, a0: int, a1: int) -> int:
        """ mod0 に対するハッシュ値 a0 と mod1 に対するハッシュ値からの混合ハッシュ値を求める.

        Args:
            a0 (int): mod0 に対するハッシュ値
            a1 (int): mod1 に対するハッシュ値

        Returns:
            int: 混合ハッシュ値
        """
        return a0 * self.__mod1 + a1

    def get(self, l: int, r: int) -> int:
        """ 連続部分列 [l, r) に関するハッシュ値を求める.

        Args:
            l (int): 左端 (閉区間)
            r (int): 右端 (開区間)

        Returns:
            int: ハッシュ値
        """

        return self.encode(self.rh0.get(l, r), self.rh1.get(l, r))

    def __hasher(self, X: Iterable[T]) -> int:
        assert len(X)<=len(self)
        a0=0; a1=0
        for x in X:
            a0 = (a0 * self.__base + self.hash_function(x)) % self.__mod0
            a1 = (a1 * self.__base + self.hash_function(x)) % self.__mod1
        return self.encode(a0, a1)

    def __getitem__(self, index):
        if index.__class__==int:
            if index<0:
                index+=self.__length
            assert 0<=index<self.__length
            return self.encode(self.rh0[index], self.rh1[index])
        elif index.__class__==slice:
            assert (index.step==None) or (index.step==1)
            L=index.start if index.start else 0
            R=index.stop if index.stop else len(self)
            if L<0:
                L+=len(self)
            if R<0:
                R+=len(self)
            return self.encode(self.rh0[L: R], self.rh1[L: R])

    def count(self, T: Iterable[T], start: int = 0) -> int:
        alpha=self.__hasher(T)
        return len([i for i in range(start, len(self) - len(T) + 1) if self[i: i + len(T)] == alpha])

    def find(self, T: Iterable[T], start: int = 0) -> int:
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def rfind(self, T: Iterable[T], start: int = 0) -> int:
        alpha=self.__hasher(T)

        for i in range(len(self)-len(T), start-1, -1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def index(self, T: Iterable[T], start: int = 0) -> int:
        ind = self.find(T, start)
        if ind == -1:
            raise ValueError("substring not found")
        return ind

    def __len__(self) -> int:
        return self.__length

    def docking(self, l0: int, r0: int, l1: int, r1: int) -> int:
        """ ranges: tuple (l,r) からなるリスト, i 番目の (l,r) は部分列 [l,r) を意味する.
        """

        return self.encode(self.rh0.docking(l0, r0, l1, r1), self.rh1.docking(l0, r0, l1, r1))

#=================================================
class Hasher():
    def __init__(self, length, base, mod, hash_function = None):
        self.length = length
        self.base = base
        self.mod = mod
        self.hash_function = hash_function = hash_function if hash_function is not None else lambda x: x

        self.power = pw = [1] * length
        for i in range(1, length):
            pw[i] = (base * pw[i - 1]) % mod

    def __repr__(self):
        return f"[Hasher] length: {self.length}, base: {self.base}, mod: {self.mod}"

    def encode(self, S):
        hash_function = self.hash_function
        N = len(S)
        code=0
        for i in range(N):
                code += hash_function(S[i]) * self.power[N - 1 - i] % self.mod

        return code % self.mod

#=================================================
class Double_Hasher():
    def __init__(self, length, base, mod0, mod1, hash_function = None):
        self.hasher_0 = Hasher(length, base, mod0, hash_function)
        self.hasher_1 = Hasher(length, base, mod1, hash_function)

    def __repr__(self):
        return f"[Double Hasher]: {self.hasher_0}, {self.hasher_1}"

    def encode(self, S):
        return self.hasher_0.encode(S) * self.hasher_1.mod + self.hasher_1.encode(S)
