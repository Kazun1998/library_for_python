class Rolling_Hash():
    def __init__(self,S, base, mod, type=0):
        """ type=0: 整数列 (各要素は mod 未満), type=1: 文字列 (mod>(最大の文字コード))

        """

        self.mod=mod
        self.base=base
        self.string=S
        self.power=power=[1]*(len(S)+1)
        self.type=type

        L=len(S)
        self.hash=h=[0]*(L+1)

        for i in range(L):
            if type:
                h[i+1]=(base*h[i]+ord(S[i]))%mod
            else:
                h[i+1]=(base*h[i]+S[i])%mod

        for i in range(L):
            power[i+1]=base*power[i]%mod

    def __hasher(self, X):
        assert len(X)<=len(self)
        h=0
        for i in range(len(X)):
            h=(h*self.base+X[i])%self.mod
        return h

    def get(self, l, r):
        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.mod

    def count(self, T, start=0):
        alpha=self.__hasher(T)

        K=0
        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                K+=1
        return K

    def find(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def rfind(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(len(self)-len(T), start-1, -1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def index(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        raise ValueError("substring not found")

    def __getitem__(self, index):
        if index.__class__==int:
            if index<0:
                index+=len(self.string)
            assert 0<=index<len(self.string)
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

    def __len__(self):
        return len(self.string)

    def docking(self, *ranges):
        """ ranges: tuple (l,r) からなるリスト, i 番目の (l,r) は部分列 [l,r) を意味する.
        """

        code=0
        for l,r in ranges:
            code=(code*self.power[r-l]+self.get(l,r))%self.mod
        return code

#=================================================
class Multi_Rolling_Hash():
    def __init__(self, S, base, mods, type):
        self.string=S
        self.__N=len(mods)
        self.__base=base
        self.__mod=mods
        self.__type=type
        self.rh=[Rolling_Hash(S, base, m, type) for m in mods]

    def get(self, l, r):
        return tuple(H[l: r] for H in self.rh)

    def __hasher(self, X):
        assert len(X)<=len(self)
        h=[0]*self.__N
        for i in range(self.__N):
            m=self.__mod[i]
            a=0
            for x in X:
                a=(a*self.__base+x)%m
            h[i]=a
        return tuple(h)

    def __getitem__(self, index):
        if index.__class__==int:
            if index<0:
                index+=len(self.string)
            assert 0<=index<len(self.string)
            return tuple(H[index] for H in self.rh)
        elif index.__class__==slice:
            assert (index.step==None) or (index.step==1)
            L=index.start if index.start else 0
            R=index.stop if index.stop else len(self)
            if L<0:
                L+=len(self)
            if R<0:
                R+=len(self)
            return tuple(H[L: R] for H in self.rh)

    def count(self, T, start=0):
        alpha=self.__hasher(T)
        K=0
        T_len=len(T)
        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+T_len]:
                K+=1
        return K

    def find(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def rfind(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(len(self)-len(T), start-1, -1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def index(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        raise ValueError("substring not found")

    def __len__(self):
        return len(self.string)

    def docking(self, *ranges):
        """ ranges: tuple (l,r) からなるリスト, i 番目の (l,r) は部分列 [l,r) を意味する.
        """

        return tuple(H.docking(*ranges) for H in self.rh)

#=================================================
class Hasher():
    def __init__(self, length, base, mod, type=0):
        self.length=length
        self.base=base
        self.mod=mod
        self.type=type

        self.power=pw=[1]*length
        for i in range(1, length):
            pw[i]=(base*pw[i-1])%mod

    def __repr__(self):
        return "length: {}\nbase: {}\nmod: {}".format(self.length, self.base, self.mod)

    def encode(self, S):
        code=0; N=len(S)
        for i in range(N):
            if self.type:
                code+=ord(S[i])*self.power[N-1-i]%self.mod
            else:
                code+=S[i]*self.power[N-1-i]%self.mod

        return code%self.mod

    def decode(self, S):
        pass
