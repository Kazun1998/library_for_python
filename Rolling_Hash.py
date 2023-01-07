class Rolling_Hash():
    def __init__(self,S, base, mod, type=0):
        """ type=0: 整数列 (各要素は mod 未満), type=1: 文字列 (mod>(最大の文字コード))

        """

        self.mod=mod
        self.base=base
        self.length=len(S)
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

    def __len__(self):
        return self.length

    def docking(self, l0, r0, l1, r1):
        """ [l0, r0) と [l1, r1) の部分列をドッキングしたハッシュを返す.
        """

        h0=self.get(l0,r0); h1=self.get(l1,r1)
        return (h0*self.power[r1-l1]+h1)%self.mod

#=================================================
class Double_Rolling_Hash():
    def __init__(self, S, base, mod0, mod1, type):
        self.__length=len(S)
        self.__base=base
        self.__mod0=mod0
        self.__mod1=mod1
        self.__type=type

        self.rh0=Rolling_Hash(S, base, mod0, type)
        self.rh1=Rolling_Hash(S, base, mod1, type)

    def encode(self, a0, a1):
        return a0*self.__mod1+a1

    def get(self, l, r):
        a0=self.rh0.get(l,r)
        a1=self.rh1.get(l,r)
        return self.encode(a0,a1)

    def __hasher(self, X):
        assert len(X)<=len(self)
        a0=0; a1=0
        for x in X:
            if self.__type==0:
                a0=(a0*self.__base+x)%self.__mod0
                a1=(a1*self.__base+x)%self.__mod1
        return self.encode(a0,a1)

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
        return self.__length

    def docking(self, l0, r0, l1, r1):
        """ ranges: tuple (l,r) からなるリスト, i 番目の (l,r) は部分列 [l,r) を意味する.
        """

        return self.encode(self.rh0.docking(l0, r0, l1, r1), self.rh1.docking(l0, r0, l1, r1))

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
