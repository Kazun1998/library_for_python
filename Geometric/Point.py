from math import sqrt,sin,cos,tan,asin,acos,atan2,pi,floor,gcd

epsilon = 1e-8
def compare(x: float, y: float, ep: float = epsilon) -> int:
    """ x,y の大小比較をする. ただし, ep の誤差は同一視する.

    Args:
        x (float):
        y (float):
        ep (float, optional): 許容誤差. Defaults to epsilon.

    Returns:
        x > y のときは 1
        x = y のときは 0
        x < y のときは -1
    """

    diff = x - y
    if diff > ep:
        return 1
    elif diff < -ep:
        return -1
    else:
        return 0

def sign(x: float, ep: float = epsilon) -> int:
    if x > ep:
        return 1
    elif x < -ep:
        return -1
    else:
        return 0

def equal(x: float, y: float, ep: float = epsilon) -> bool:
    return abs(x - y) < ep

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    #文字列
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    #Bool
    def __bool__(self):
        return (sign(self.x) != 0) or (sign(self.y) != 0)

    #等号
    def __eq__(self, other: "Point") -> bool:
        return (compare(self.x, other.x) == 0) and (compare(self.y, other.y) == 0)

    #不等号
    def __ne__(self, other: "Point") -> bool:
        return not (self == other)

    #比較(<)
    def __lt__(self, other: "Point") -> bool:
        if (t := compare(self.x, other.x)):
            return t < 0
        return compare(self.y, other.y) < 0

    #比較(<=)
    def __le__(self, other: "Point") -> bool:
        return self < other or self == other

    #比較(>)
    def __gt__(self, other: "Point") -> bool:
        return other < self

    #比較(>=)
    def __ge__(self, other: "Point") -> bool:
        return other <= self

    #正と負
    def __pos__(self) -> "Point":
        return self

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)

    #加法
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: "Point") -> "Point":
        self.x += other.x
        self.y += other.y
        return self

    #減法
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other: "Point") -> "Point":
        self.x -= other.x
        self.y -= other.y
        return self

    #乗法
    def __mul__(self, other: "Point") -> "Point":
        x, y = self.x, self.y
        u, v = other.x, other.y
        return Point(x * u- y * v, x * v + y * u)

    def __imul__(self, other: "Point") -> "Point":
        return other * self

    def __rmul__(self, other: int | float) -> "Point":
        if isinstance(other, (int, float)):
            return Point(other * self.x, other * self.y)
        raise NotImplemented

    #除法
    def __truediv__(self, other) -> "Point":
        if other == 0:
            raise ZeroDivisionError
        return Point(self.x / other, self.y / other)

    #絶対値
    def __abs__(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)

    norm = __abs__

    def norm_2(self) -> float:
        """ ノルムの 2 乗を求める

        Returns:
            float: ノルムの 2 乗
        """
        return self.x * self.x + self.y * self.y

    #回転
    def rotate(self, theta: float) -> "Point":
        """ 原点中心に theta だけ回転させた後の点を求める.

        Args:
            theta (float): 回転角

        Returns:
            Point: 回転後の点
        """
        x, y = self.x, self.y
        s, c = sin(theta), cos(theta)
        return Point(c * x - s * y , s * x + c * y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __hash__(self):
        return hash((self.x,self.y))

    def latticization(self, delta: float = 1e-7):
        """ 点が格子点に十分近いとき, この点を格子点の点として修正する.

        Args:
            delta (float, optional): 判断のための閾値. Defaults to 1e-7.
        """

        if (abs(self.x - floor(self.x + 0.5)) < delta) and (abs(self.y-floor(self.y + 0.5)) < delta):
            self.x = floor(self.x+0.5)
            self.y = floor(self.y+0.5)

    def normalization(self):
        """ 向きをそのままに, 長さを 1 に変換する.
        """

        r = abs(self)
        self.x /= r
        self.y /= r

    def normal_unit_vector(self) -> "Point":
        """ 単位法線ベクトルを求める.

        Returns:
            Point: 単位法線ベクトル
        """

        assert self, ValueError

        d = self.norm()
        return Point(-self.y / d, self.x / d)

    def dot(self, other: "Point") -> float:
        """ 内積を求める

        Args:
            other (Point):

        Returns:
            Point: 内積
        """
        return self.x * other.x + self.y * other.y

    def det(self, other: "Point") -> float:
        """ 外積を求める

        Args:
            other (Point):

        Returns:
            float: 外積
        """

        return self.x * other.y - self.y * other.x

    def arg(self) -> float:
        """ 原点からみたこの点の偏角

        Returns:
            float: 偏角
        """

        return atan2(self.y,self.x)

    def copy(self):
        return Point(self.x,self.y)

def iSP(A: Point, B: Point, C: Point) -> int:
    """ A->B->C と進んだときの進行方向を見る. ※ B が中心

    Args:
        A (Point): 始点
        B (Point): 中継点
        C (Point): 終点

    Returns:
        int:
            左折 (反時計回り): +1
            右折 (時計回り): -1
            C-A-B の順に並んでいる: -2
            A-B-C の順に並んでいる: 2
            A-C-B の順に並んでいる: 0
    """

    if (p := sign((B - A).det(C - A))) != 0:
        return p

    if sign((B - A).dot(C - A)) == -1:
        return -2
    if sign((A - B).dot(C - B)) == -1:
        return 2
    return 0

def Arg(P: Point, Q: Point = Point(0,0)) -> float:
    """ 点 Q から見た点 P の偏角を求める.

    Args:
        P (Point): 点
        Q (Point, optional): 基準点. Defaults to Point(0,0).

    Returns:
        float: 偏角
    """

    R = P - Q
    return atan2(R.y, R.x)

def Angle_Type(A: Point, B: Point, C: Point) -> int:
    """ 角ABC が鋭角か直角か鈍角かを判定する.

    Args:
        A (Point):
        B (Point):
        C (Point):

    Returns:
        int:
            1: 鋭角
            0: 直角
            -1: 鈍角
    """

    return sign((A-B).dot(C-B))

def Inner(P: Point, Q: Point) -> float:
    """ 点 P と点 Q の内積を求める.

    Args:
        P (Point):
        Q (Point):

    Returns:
        float: 内積
    """

    return P.x * Q.x + P.y * Q.y

def Det(P: Point, Q: Point) -> float:
    """ 点 P と点 Q が貼る平行四辺形の符号付き面積 (外積) を求める.

    Args:
        P (Point):
        Q (Point):

    Returns:
        float: 外積
    """

    return P.x * Q.y - P.y * Q.x

def Internal_Division_Point(P: Point, Q: Point, a: float, b: float) -> Point:
    """ 線分 PQ を a:b に内分する点を求める.

    Args:
        P (Point):
        Q (Point):
        a (float): P 側の比率
        b (float): Q 側の比率

    Returns:
        Point: 線分 PQ を a:b に内分する点を求める
    """

    assert a + b != 0

    return (b * P + a * Q) / (a + b)

def External_Division_Point(P: Point, Q: Point, a: float, b: float) -> Point:
    """ 線分 PQ を a:b に外分する点を求める.

    Args:
        P (Point):
        Q (Point):
        a (float): P 側の比率
        b (float): Q 側の比率

    Returns:
        Point: 線分 PQ を a:b に内分する点を求める
    """

    assert a - b != 0
    return (-b * P + a * Q) / (a - b)

def MidPoint(P: Point, Q: Point) -> Point:
    """ 線分 PQ の中点を求める.

    Args:
        P (Point):
        Q (Point):

    Returns:
        Point: 中点
    """

    return Point((P.x + Q.x) / 2, (P.y + Q.y) / 2)

def Argument_Compare(P: Point, Q: Point)  -> bool:
    """ OQ が OP からみて反時計回りかどうか?

    Args:
        P (Point): 基準点
        Q (Point): 判定点

    Returns:
        bool: 反時計回りならば True
    """
    return sign(Q.det(P))

def Argument_Sort(L):
    """ 点を偏角ソートする.

    L: 点のリスト
    """

    from functools import cmp_to_key

    def position(P):
        m=compare(P.y,0)
        if m==-1:
            return -1
        elif m==0 and compare(P.x,0)>=0:
            return 0
        else:
            return 1

    def cmp(P,Q):
        a=position(P); b=position(Q)
        if a<b: return -1
        elif a>b: return 1
        else:return -compare(P.det(Q),0)

    L.sort(key=cmp_to_key(cmp))

def Argument_Sort_by_Index(L):
    """ 点を偏角ソートする (返り値は添字).

    L: 点のリスト
    """

    def merge(a,b):
        I=[]

        la=len(a); lb=len(b)
        ia=0; ib=0

        while (ia<la) and (ib<lb):
            if Argument_Compare(L[a[ia]],L[b[ib]])<=0:
                I.append(a[ia])
                ia+=1
            else:
                I.append(b[ib])
                ib+=1

        for i in range(ia,la):
            I.append(a[i])

        for i in range(ib,lb):
            I.append(b[i])

        return I

    def sorting(a):
        if len(a)==1:
            return a
        else:
            return merge(sorting(a[:len(a)//2]),sorting(a[len(a)//2:]))

    return sorting(list(range(len(L))))
