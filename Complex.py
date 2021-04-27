import math

class Complex(Fraction):
    #入力定義
    def __init__(self,Real_part=0,Imaginary_part=0):
        self.re=Real_part
        self.im=Imaginary_part

    #表示定義
    def __str__(self):
        s=""
        s=Complex.__strmake(s,self.re,"")
        s=Complex.__strmake(s,self.im,"i")
        if s=="":
            return "0"
        else:
            return s

    def __strmake(self,coefficient,axis):
        if coefficient==0:
            return self
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
        c=Complex()
        if not(isinstance(other,Complex)):
            other=Complex.Real_Complex(other)
        c.re=self.re+other.re
        c.im=self.im+other.im
        return c

    def __radd__(self,other):
        c=Complex()
        if not(isinstance(other,Complex)):
            other=Complex.Real_to_Complex(other)
        c.re=self.re+other.re
        c.im=self.im+other.im
        return c
    
    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        c=Complex()
        if not(isinstance(other,Complex)):
            other=Complex.Real_to_Complex(other)
        c.re=self.re*other.re-self.im*other.im
        c.im=self.re*other.im+self.im*other.re
        return c

    def __rmul__(self,other):
        c=Complex()
        if not(isinstance(other,Complex)):
            other=Complex.Real_to_Complex(other)
        c.re=self.re*other.re-self.im*other.im
        c.im=self.re*other.im+self.im*other.re
        return c

    def __truediv__(self,other):
        if not(isinstance(other,(Complex))):
            other=Complex.Real_to_Complex(other)
        return self*Complex.__inverse(other)

    def __rtruediv__(self,other):
        if not(isinstance(other,(Complex))):
            other=Complex.Real_to_Complex(other)
        return Complex.__inverse(self)*other

    #比較演算子
    def __eq__(self,other):
        return (self-other)==Complex()
        
    #その他
    def conjugate(self):
        return Complex(self.re,-self.im)

    def __abs__(self):
        return math.sqrt((self*Complex.conjugate(self)).re)

    def abs2(self):
        return (self*Complex.conjugate(self)).re

    #実数から複素数に変換
    def Real_to_Complex(self):
        if not(isinstance(self,Complex)):
            return Complex(self,0)
        else:
            return self
    
    #正負判定

    #要約

    #逆数
    def __inverse(self):
        return Fraction(1,Complex.abs2(self))*Complex.conjugate(self)

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Complex(-self.re,-self.im)
