class Polynominal_Error(Exception):
    pass

class Polynominal():
    def __init__(self,P=[],C="X"):
        self.Poly=P
        self.Char=C

    def __str__(self):
        S=""
        flag=False
        
        for k in range(len(self.Poly)):
            if self.Poly[k]:
                if flag:
                    if k==1:
                        S+="{:+}{}".format(self.Poly[1],self.Char)
                    else:
                        S+="{:+}{}^{}".format(self.Poly[k],self.Char,k)
                else:
                    flag=True
                    if k==0:
                        S=str(self.Poly[0])
                    elif k==1:
                        S=str(self.Poly[1])+self.Char
                    else:
                        S=str(self.Poly[k])+"{}^{}".format(self.Char,k)

        if S:
            return S
        else:
            return "0"

    #+,-
    def __pos__(self):
        return self

    def __neg__(self):
        return self.scale(-1)

    #Boole
    def __bool__(self):
        return not(self.reduce().Poly==[0])
    #簡略化
    def reduce(self):
        P_deg=self.degree()
        
        if not(P_deg>=0):
            return Polynominal([0],self.Char)
            
        for i in range(self.degree(),-1,-1):
            if self.Poly[i]:
                return Polynominal(self.Poly[:i+1],self.Char)
        
    #次数
    def degree(self):
        x=-float("inf")
        k=0
        for y in self.Poly:
            if y!=0:
                x=k
            k+=1
        return x

    #加法
    def __add__(self,other):
        if isinstance(other,Polynominal):
            P_deg=max(self.degree(),0)
            Q_deg=max(other.degree(),0)
            R=[0]*(min(P_deg,Q_deg)+1)

            for k in range(min(P_deg,Q_deg)+1):
                R[k]=self.Poly[k]+other.Poly[k]

            if P_deg>=Q_deg:
                R+=self.Poly[Q_deg+1:]
            else:
                R+=other.Poly[P_deg+1:]

            return Polynominal(R,self.Char).reduce()
        else:
            P_deg=self.degree()
            R=[0]*(P_deg+1)
            
            for i in range(P_deg+1):
                if i:
                    R[i]=self.Poly[i]
                else:
                    R[i]=self.Poly[i]+other

            return Polynominal(R,self.Char).reduce()

    def __radd__(self,other):
        return self+other

    #減法
    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return (-self)+other
    
    #乗法
    def __mul__(self,other):
        if self==0 or other==0:
            return Polynominal([0],self.Char)

        if isinstance(other,Polynominal):
            P_deg=max(self.degree(),0)
            Q_deg=max(other.degree(),0)

            R=[0]*(P_deg+Q_deg+1)

            for i in range(P_deg+1):
                for j in range(Q_deg+1):
                    R[i+j]+=self.Poly[i]*other.Poly[j]
            return Polynominal(R,self.Char).reduce()
        else:
            return self.scale(other)

    def __rmul__(self,other):
        return self.scale(other)

    #除法
    def __floordiv__(self,other):
        if not other:
            raise ZeroDivisionError

        pass

    #剰余
    def __mod__(self,other):
        return self-(self//other)*other

    #累乗
    def __pow__(self,n):
        if n<0:
            raise  Polynominal_Error("nが負です.")

        R=Polynominal([1],self.Char)
        P=self
        
        while n>0:
            if n%2:
                R*=P
            P*=P
            n=n>>1
                
        return R
    
    #スカラー倍
    def scale(self,s):
        P_deg=self.degree()
        
        Q=[0]*(P_deg+1)
        for i in range(P_deg+1):
            Q[i]=s*self.Poly[i]

        return Polynominal(Q,self.Char).reduce()

    #係数
    def coefficient(self,n):
        try:
            if n<0:
                raise IndexError

            return self.Poly[n]
        except IndexError:
            return  0
        except TypeError:
            return 0

    #最高次の係数
    def leading_coefficient(self):
        for x in self.Poly[::-1]:
            if x:
                return x
        return 0
    
    #代入
    def substitute(self,a):
        x=1
        P_deg=self.degree()

        S=0
        for i in range(P_deg+1):
            S+=self.Poly[i]*x
            x*=a
        return S

#最大公約数
def gcd(P,Q):
    """Gauss整数 x,yの最大公約数を求める.

    x,y:Gauss整数
    """

    if P.degree()<Q.degree():
        P,Q=Q,P

    while Q:
        P.Q=Q,P%Q

    return P

#拡張Euclidの互除法
def Extended_Euclid(x,y):
    """拡張Euclidの互除法を用いて,xa+yb=gcd(x,y)を満たすGauss整数a,bを求める.

    x,y:Gauss整数

    [出力]:(a,b,gcd(x,y))
    """

    a0,b0,a1,b1=1,0,0,1
    while y:
        q,x,y=x//y,y,x%y
        a0,a1=a1,a0-q*a1
        b0,b1=b1,b0-q*b1
    return a0,b0,x
    
