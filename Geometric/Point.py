from Common import Common, sign, compare
from math import sqrt,sin,cos,tan,asin,acos,atan2,pi,floor,gcd

class Point(Common):
    __slots__=("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #文字列
    def __str__(self):
        return f"({self.x}, {self.y})".format(self.x, self.y)

    __repr__=__str__

    def __iter__(self):
        yield self.x
        yield self.y

    #Bool
    def __bool__(self):
        return sign(self.x) != 0 or sign(self.y) != 0

    #等号
    def __eq__(self, other):
        return compare(self.x, other.x) == 0 and compare(self.y, other.y) == 0

    #不等号
    def __ne__(self, other):
        return not self == other

    #比較(<)
    def __lt__(self, other):
        sign_x = compare(self.x, other.x)

        if sign_x == -1:
            return True
        elif sign_x == 1:
            return False
        else:
            return compare(self.y, other.y) == -1

    #比較(<=)
    def __le__(self, other):
        return self < other or self == other

    #比較(>)
    def __gt__(self, other):
        return other < self

    #比較(>=)
    def __ge__(self, other):
        return other <= self

    #正と負
    def __pos__(self):
        return self

    def __neg__(self):
        return Point(-self.x, -self.y)

    #加法
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    #減法
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    #乗法
    def __mul__(self, other):
        x, y = self
        u, v = other
        return Point(x * u - y * v, x * v + y * u)

    def __imul__(self, other):
        return other * self

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Point(other * self.x, other * self.y)

    #除法
    def __truediv__(self, other):
        if other==0:
            raise ZeroDivisionError
        return Point(self.x / other, self.y / other)

    #絶対値
    def __abs__(self):
        x,y = self
        return sqrt(self.x * self.x + self.y * self.y)

    norm=__abs__

    def norm_2(self):
        return self.x * self.x + self.y * self.y

    #回転
    def rotate(self, theta):
        x, y = self
        s, c = sin(theta), cos(theta)
        return Point(c * x - s * y, s * x + c * y)

    def __hash__(self):
        return hash((self.x, self.y))

    def latticization(self, delta):
        """ 格子点に十分近いならば, その格子点に吸い寄せる"""

        ax = floor(self.x + 0.5); ay = floor(self.y + 0.5)

        if compare(abs(self.x - ax), delta) <= 0 and compare(abs(self.y - ay), delta) <= 0:
            self.x = ax
            self.y = ay
            return True
        return False

    def normalization(self):
        a = abs(self)
        self.x /= a
        self.y /= a

    def normal_unit_vector(self):
        """ 単位法線ベクトルを求める"""

        assert self
        d=self.norm()
        return Point(-self.y / d, self.x / d)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def det(self, other):
        return self.x * other.y - self.y * other.x

    def arg(self):
        return atan2(self.y, self.x)

    def copy(self):
        return Point(self.x, self.y)

def Distance(A,B):
    return abs(A-B)

def iSP(A,B,C):
    """ A->B->C と進んだときの進行方向を見る. ※ B が中心

    A,B,C: Point

    左折 (反時計回り):+1
    右折 (時計回り)   :-1
    C-A-Bの順に並んでいる: -2
    A-B-Cの順に並んでいる: 2
    A-C-Bの順に並んでいる: 0
    """

    p = compare((B-A).det(C-A), 0)
    if p == 1:
        return 1
    elif p == -1:
        return -1
    else:
        if compare((B-A).dot(C-A), 0) == -1:
            return -2
        elif compare((A-B).dot(C-B), 0) == -1:
            return 2
        return 0

def Arg(P,Q=Point(0,0)):
    """点 Q から見た点 P の偏角を求める.

    P,Q: Point
    """

    R=P-Q
    return atan2(R.y,R.x)

def Angle_Type(A,B,C):
    """ 角ABC が鋭角か直角か鈍角かを判定する.

    [Input]
    A,B,C: Point

    [Output]
    1: 鋭角, 0: 直角, -1: 鈍角
    """

    return compare((A-B).dot(C-B), 0)

def Inner(P,Q):
    """点P,Qの内積を求める.

    P,Q:Point
    """
    return P.x*Q.x+P.y*Q.y

def Det(P,Q):
    """点P,Qが張る平行四辺形の符号付き面積を求める.

    P,Q:Point
    """
    return P.x*Q.y-P.y*Q.x

def Internal_Division_Point(P,Q,p,q):
    """線分PQをp:qに内分する点を求める.

    P,Q:Point
    p,q:int or float
    """
    assert p+q
    return (q*P+p*Q)/(p+q)

def External_Division_Point(P,Q,p,q):
    """線分PQをp:qに内分する点を求める.

    P,Q:Point
    p,q:int or float
    """
    assert p-q
    return (-q*P+p*Q)/(p-q)

def MidPoint(P,Q):
    """線分PQの中点を求める.

    P,Q:Point
    """
    a=(P.x+Q.x)/2
    b=(P.y+Q.y)/2
    return Point(a,b)

def Argument_Compare(P,Q):
    """ OQ が OP からみて反時計回りかどうかを判定する."""
    return compare(Q.det(P), 0) > 0

def Argument_Sort(L):
    """ 点を偏角ソートする.

    L: 点のリスト
    """

    from functools import cmp_to_key

    def position(P):
        m = compare(P.y, 0)
        if m == -1:
            return -1
        elif m == 0 and compare(P.x, 0)>=0:
            return 0
        else:
            return 1

    def cmp(P, Q):
        a = position(P); b = position(Q)
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return -compare(P.det(Q), 0)

    L.sort(key = cmp_to_key(cmp))

def Argument_Sort_by_Index(L):
    """ 点を偏角ソートする (返り値は添字).

    L: 点のリスト
    """

    def position(P):
        m = compare(P.y, 0)
        if m == -1:
            return -1
        elif m == 0 and compare(P.x, 0) >= 0:
            return 0
        else:
            return 1

    def merge(a, b):
        I = []

        la = len(a); lb = len(b)
        ia = 0; ib = 0

        while (ia < la) and (ib < lb):
            if Argument_Compare(L[a[ia]], L[b[ib]]) <= 0:
                I.append(a[ia])
                ia += 1
            else:
                I.append(b[ib])
                ib += 1

        I.extend(a[ia:])
        I.extend(b[ib:])

        return I

    def sorting(a):
        if len(a) <= 1:
            return a
        else:
            return merge(sorting(a[:len(a)//2]), sorting(a[len(a)//2:]))

    I=[]; J=[]; K=[]
    for i in range(len(L)):
        match position(L[i]):
            case 1:
                I.append(i)
            case 0:
                J.append(i)
            case -1:
                K.append(i)
    return sorting(K) + J + sorting(I)
