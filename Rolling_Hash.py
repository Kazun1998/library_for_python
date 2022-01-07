class Rolling_Hash():
    def __init__(self,S,Base,Mod):
        self.Mod=Mod
        self.Base=Base
        self.string=S
        self.power=power=[1]*(len(S)+1)

        L=len(S)
        self.hash=h=[0]*(L+1)

        v=0
        for i in range(L):
            #h[i+1]=v=(v*Base+ord(S[i]))%Mod
            h[i+1]=v=(v*Base+S[i])%Mod

        v=1
        for i in range(L):
            power[i+1]=v=(v*Base)%Mod

    def get(self,l,r):
        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.Mod

    def count(self,T,start=0):
        alpha=0
        for t in T:
            alpha=(alpha*self.Base+ord(t))%self.Mod

        K=0
        for i in range(start,len(self)-len(T)+1):
            if alpha==self[i:i+len(T)]:
                K+=1
        return K

    def find(self,T,start=0):
        alpha=0
        for t in T:
            alpha=(alpha*self.Base+ord(t))%self.Mod

        for i in range(start,len(self)-len(T)+1):
            if alpha==self[i:i+len(T)]:
                return i
        return -1

    def rfind(self,T,start=0):
        alpha=0
        for t in T:
            alpha=(alpha*self.Base+ord(t))%self.Mod

        for i in range(len(self)-len(T),start-1):
            if alpha==self[i:i+len(T)]:
                return i
        return -1

    def index(self,T,start=0):
        alpha=0
        for t in T:
            alpha=(alpha*self.Base+ord(t))%self.Mod

        for i in range(start,len(self)-len(T)+1):
            if alpha==self[i:i+len(T)]:
                return i
        raise ValueError("substring not found")

    def index(self,T,start=0):
        alpha=0
        for t in T:
            alpha=(alpha*self.Base+ord(t))%self.Mod

        for i in range(len(self)-len(T),start-1):
            if alpha==self[i:i+len(T)]:
                return i
        raise ValueError("substring not found")

    def __getitem__(self,index):
        if index.__class__==int:
            if index<0:
                index+=len(self.string)
            assert 0<=index<len(self.string)
            return self.get(index,index+1)
        elif index.__class__==slice:
            assert (index.step==None) or (index.step==1)
            L=index.start if index.start else 0
            R=index.stop if index.stop else len(self)
            if L<0:L+=len(self)
            if R<0:R+=len(self)
            return self.get(L,R)

    def __len__(self):
        return len(self.string)

#=================================================
class Hasher():
    def __init__(self, length, base, mod):
        self.length=length
        self.base=base
        self.mod=mod

        self.power=pw=[1]*length
        for i in range(1,length):
            pw[i]=(base*pw[i-1])%mod

    def __repr__(self):
        return "length: {}\nbase: {}\nmod: {}".format(self.length, self.base, self.mod)

    def encode(self, S):
        code=0; N=len(S)
        for i in range(N):
            code+=ord(S[i])*self.power[N-1-i]%self.mod
            #code+=S[i]*self.power[N-1-i]%self.mod

        return code%self.mod

    def decode(self, S):
        pass
