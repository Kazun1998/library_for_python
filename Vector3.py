import math
from Fraction import Fraction
from Complex import Complex
from Quaternion import Quaternion

class Vector3(Quaternion):
    #入力定義
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    #表示定義
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    #四則演算定義
    def __add__(self,other):
        v=Vector3()
        v.x=self.x+other.x
        v.y=self.y+other.y
        v.z=self.z+other.z
        return v

    def __radd__(self,other):
        v=Vector3()
        v.x=self.x+other.x
        v.y=self.y+other.y
        v.z=self.z+other.z
        return v

    def __sub__(self,other):
        return self+(-other)

    def __rsub__(self,other):
        return -self+other

    def __mul__(self,other):
        v=Vector3()
        v.x=self.x*other.x
        v.y=self.y*other.y
        v.z=self.z*other.z
        return v

    def __rmul__(self,other):
        v=Vector3()
        v.x=self.x*other.x
        v.y=self.y*other.y
        v.z=self.z*other.z
        return v

    def __truediv__(self,other):
        return self*Vector3.__inverse(other)

    def __rtruediv__(self,other):
        return Vector3.__inverse(self)*other

    def scaling(self,scale):
        s=Vector3(scale,scale,scale)
        return self*s

    #比較演算子
    def __eq__(self,other):
        return (self-other)==Vector3()

    #その他
    def inner(self,other):
        r=Quaternion()
        r+=Quaternion.conjugate(self.x)*other.x
        r+=Quaternion.conjugate(self.y)*other.y
        r+=Quaternion.conjugate(self.z)*other.z
        return r.r

    def cross(self,other):
        v=Vector3()
        v.x=self.y*other.z-self.z*other.y
        v.y=self.z*other.x-self.x*other.z
        v.z=self.x*other.y-self.y*other.x
        return v

    def __abs__(self):
        return math.sqrt(Vector3.inner(v,v))

    def abs2(self):
        return Vector3.inner(v,v)

    def internal(self,other,m,n):
        if m==-n:
            return Vector3.scaling(Vector3.scaling(other,m)+Vector3.scaling(self,n),Fraction(1,m+n))

        else:
            print("Cannot internal divide",m,":",n,"!")
            return Vector3()

    def external(self,other,m,n):
        if m!=n:
            return Vector3.internal(self,other,m,-n)

        else:
            print("Cannot external divide",m,":",n,"!")
            return Vector3()

    def middle(self,other):
        return Vector3.internal(self,other,1,1)

    #正負判定

    #要約

    #逆数
    def __inverse(self):
        v=Vector3()
        if self.x!=0:v.x=1/self.x
        else:v.x=0
        if self.y!=0:v.y=1/self.y
        else:v.y=0
        if self.z!=0:v.z=1/self.z
        else:v.z=0

        return v

    #符号
    def __pos__(self):
        return self

    def __neg__(self):
        return Vector3(-self.x,-self.y,-self.z)




