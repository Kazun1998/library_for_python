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

#=================================================
class Double_Hasher():
    def __init__(self, length, base, mod0, mod1, type=0):
        self.length=length
        self.base=base
        self.mod0=mod0
        self.mod1=mod1
        self.type=type

        self.power0=pw0=[1]*length
        self.power1=pw1=[1]*length
        for i in range(1, length):
            pw0[i]=(base*pw0[i-1])%mod0
            pw1[i]=(base*pw1[i-1])%mod1

    def __repr__(self):
        return "length: {}\nbase: {}\nmod: {}".format(self.length, self.base, self.mod)

    def encode(self, S):
        code0=0; code1=0
        N=len(S)
        for i in range(N):
            if self.type:
                code0+=ord(S[i])*self.power0[N-1-i]%self.mod0
                code1+=ord(S[i])*self.power1[N-1-i]%self.mod1
            else:
                code0+=S[i]*self.power0[N-1-i]%self.mod0
                code1+=S[i]*self.power1[N-1-i]%self.mod1

        code0%=self.mod0; code1%=self.mod1
        return code1*self.mod0+code0
