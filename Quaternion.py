import math
from Fraction import Fraction
#from Complex import Complex

class Quaternion(Complex):
    #入力定義
    def __init__(self,Real_part=0,Imaginary_part_i=0,Imaginary_part_j=0,Imaginary_part_k=0):
        self.r=Real_part
        self.i=Imaginary_part_i
        self.j=Imaginary_part_j
        self.k=Imaginary_part_k

    #表示定義
    def __str__(self):
        s=""
        s=Quaternion.__strmake(s,self.r,"")
        s=Quaternion.__strmake(s,self.i,"i")
        s=Quaternion.__strmake(s,self.j,"j")
        s=Quaternion.__strmake(s,self.k,"k")
        if s=="":return "0"
        else:return s

    def __strmake(self,coefficient,axis):
        if coefficient==0:return self
        else:
            if self=="":
                if axis=="":
                    self+=str(coefficient)
                else:
                    if coefficient==1:self+=axis
                    elif coefficient==-1:self+="-"+axis
                    else:self+=str(coefficient)+axis
            else:
                if coefficient>0:
                    if coefficient==1:self+="+"+axis
                    else:self+="+"+str(coefficient)+axis
                else:
                    if coefficient==-1:self+="-"+axis
                    else:self+=str(coefficient)+axis

        return self

    #四則演算定義
    def __add__(self,other):
        q=Quaternion()
        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)
        q.r=self.r+other.r
        q.i=self.i+other.i
        q.j=self.j+other.j
        q.k=self.k+other.k
        return q

    def __radd__(self,other):
        q=Quaternion()
        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)
        q.r=self.r+other.r
        q.i=self.i+other.i
        q.j=self.j+other.j
        q.k=self.k+other.k
        return q

    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        q=Quaternion()
        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)
        s=self
        o=other
        q.r=s.r*o.r-s.i*o.i-s.j*o.j-s.k*o.k
        q.i=s.r*o.i+s.i*o.r+s.j*o.k-s.k*o.j
        q.j=s.r*o.j+s.j*o.r+s.k*o.i-s.i*o.k
        q.k=s.r*o.k+s.k*o.r+s.i*o.j-s.j*o.i
        return q

    def __rmul__(self,other):
        q=Quaternion()
        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)
        s=self
        o=other
        q.r=s.r*o.r-s.i*o.i-s.j*o.j-s.k*o.k
        q.i=s.r*o.i+s.i*o.r+s.j*o.k-s.k*o.j
        q.j=s.r*o.j+s.j*o.r+s.k*o.i-s.i*o.k
        q.k=s.r*o.k+s.k*o.r+s.i*o.j-s.j*o.i
        return q

    def __truediv__(self,other):
        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)
        return self*Quaternion.__inverse(other)

    def __rtruediv__(self,other):
        if not(isinstance(other,Quaternion)):other=Quaternion.Complex_to_Quatrarnion(other)
        return Quaternion.__inverse(self)*other

    #比較演算子
    def __eq__(self,other):
        return (self-other)==Quaternion()

    #その他
    def conjugate(self):
        self=Quaternion.Complex_to_Quatrarnion(self)
        return Quaternion(self.r,-self.i,-self.j,-self.k)

    def __abs__(self):
        return math.sqrt((self*Quaternion.conjugate(self)).r)

    def abs2(self):
        return (self*Quaternion.conjugate(self)).r

    #複素数から四元数に変換
    def Complex_to_Quatrarnion(self):
        if not(isinstance(self,Quaternion)):
            #if not(isinstance(self,Complex)):self=Complex.Real_to_Complex(self)
            return Quaternion(self.re,self.im,0,0)
        else:
            return self

    #正負判定

    #要約

    #逆数
    def __inverse(self):
        return  Fraction(1,Quaternion.abs2(self))*Quaternion.conjugate(self)

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Quaternion(-self.r,-self.i,-self.j,-self.k)
