""" Bitset 説明書
事前に N (Biset のサイズ) と __bit_size (各ブロックごとに収めるサイズ) を決めなくてはいけない.

[おすすめ]
N=10^5, __bit_size=N//k (4<=k<=10)
N=3000, __bit_size=63?

※ count, len を使いたい場合は __bit_size=63 でないと使えない!!!
"""

class Bitset:
    def __popcount(self, n):
        n -= ((n >> 1) & 0x5555555555555555)
        n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
        n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
        n += ((n >> 8) & 0x00ff00ff00ff00ff)
        n += ((n >> 16) & 0x0000ffff0000ffff)
        n += ((n >> 32) & 0x00000000ffffffff)
        return n & 0x7f

    # ※ 事前に設定しておくこと!!!
    N=30
    __bit_size=63*1
    # ここまで

    __block=(N+__bit_size-1)//__bit_size

    __msk_b=(1<<__bit_size)-1
    __msk_s=(1<<(N%__bit_size))-1

    __on=[1<<i for i in range(__bit_size)]
    __off=[0]*__block
    for k in range(__block):
        __off[k]=((1<<__bit_size)-1) & (1<<k)

    def __init__(self):
        self.__bit=[0]*self.__block

    def __len__(self):
        assert self.__bit_size<=63
        x=0
        for bit in self.__bit:
            x+=self.__popcount(bit)
        return x

    def __str__(self):
        return " ".join(map(str, [i for i in range(self.N) if i in self]))

    def __repr__(self):
        return "[Bitset] : "+str(self)

    def __contains__(self, index):
        k,i=divmod(index, self.__bit_size)
        return bool((self.__bit[k]>>i)&1)

    __getitem__=__contains__
    def __setitem__(self, index, value):
        self.set(index, value)

    def set(self, index=-1, value=1):
        if index==-1:
            if value:
                self.__bit[-1]=self.__msk_s
                for k in range(self.__block):
                    self.__bit[k]=self.__msk_b
            else:
                for k in range(self.__block):
                    self.__bit[k]=0
        else:
            k,i=divmod(index, self.__bit_size)
            if value:
                self.__bit[k]|=self.__on[i]
            else:
                self.__bit[k]&=self.__off[i]

    def reset(self, index=-1):
        self.set(index,value=0)

    def flip(self, index=-1):
        if index==-1:
            for k in range(self.__block-1):
                self.__bit[k]=self.__bit[k]^self.__msk_b
            if self.N%self.__bit_size:
                self.__bit[-1]=self.__bit[-1]^self.__msk_s
            else:
                self.__bit[-1]=self.__bit[-1]^self.__msk_b
        else:
            k,i=divmod(index, self.__bit_size)
            self.__bit[k]^=self.__on[i]

    test=__contains__

    def any(self):
        for bit in self.__bit:
            if bit:
                return True
        return False

    def all(self):
        for k in range(self.__block-1):
            if self.__bit[k]!=self.__msk_b:
                return False
        if self.N%self.__bit_size:
            return self.__bit[-1]==self.__msk_s
        else:
            return self.__bit[-1]==self.__msk_b

    def __iand__(self, other):
        for k in range(self.__block):
            self.__bit[k]&=other.__bit[k]
        return self

    def __and__(self, other):
        X=self.copy()
        X&=other
        return X

    def __ior__(self, other):
        for k in range(self.__block):
            self.__bit[k]|=other.__bit[k]
        return self

    def __or__(self, other):
        X=self.copy()
        X|=other
        return X

    def __ixor__(self, other):
        for k in range(self.__block):
            self.__bit[k]^=other.__bit[k]
        return self

    def __xor__(self, other):
        X=self.copy()
        X^=other
        return X

    def __eq__(self, other):
        for k in range(self.__block):
            if self.__bit[k]!=other.__bit[k]:
                return False
        return True

    def __neq__(self, other):
        return not(self==other)

    def copy(self):
        X=Bitset()
        X.__bit=self.__bit.copy()
        return X

    count=__len__
