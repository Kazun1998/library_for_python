from Point import *

class Triangle():
    __slots__ = ('A', 'B', 'C')

    def __init__(self, A: Point, B: Point, C: Point):
        """ 3 点 A, B, C を頂点とする三角形を生成する.

        Args:
            A (Point):
            B (Point):
            C (Point):
        """

        self.A = A
        self.B = B
        self.C = C

    def __str__(self) -> str:
        return f"[Triangle] {self.A}, {self.B}, {self.C}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.A}, {self.B}, {self. C})"

    def area(self) -> float:
        return abs((self.B - self.A).det(self.C - self.A) / 2)

    def three_edges(self) -> tuple[float, float, float]:
        """ 辺 BC, 辺 CA, 辺 AB の長さを出力する.

        Returns:
            tuple[float, float, float]: 辺 BC, 辺 CA, 辺 AB の長さのタプル
        """

        return abs(self.B - self.C), abs(self.C - self.A), abs(self.A - self.B)

#=== 三角形の心
def Center_of_Gravity(T: Triangle) -> Point:
    """ 三角形 T の重心を求める

    Args:
        T (Triangle): 三角形

    Returns:
        Point: 三角形 T の重心
    """

    return (T.A + T.B + T.C) / 3

def CircumCenter(T: Triangle) -> Point:
    """ 三角形 T の外心を求める

    Args:
        T (Triangle): 三角形

    Returns:
        Point: 三角形 T の外心
    """

    da=(T.B-T.C).norm_2()
    db=(T.C-T.A).norm_2()
    dc=(T.A-T.B).norm_2()
    ta=da*(-da+db+dc)
    tb=db*(da-db+dc)
    tc=dc*(da+db-dc)
    s=ta+tb+tc
    return (ta/s)*T.A+(tb/s)*T.B+(tc/s)*T.C

def InnerCenter(T: Triangle) -> Point:
    """ 三角形 T の内心を求める

    Args:
        T (Triangle): 三角形

    Returns:
        Point: 三角形 T の内心
    """

    a,b,c=T.three_edges()
    return (a*T.A+b*T.B+c*T.C)/(a+b+c)

def OrthoCenter(T: Triangle) -> Point:
    """ 三角形 T の垂心を求める

    Args:
        T (Triangle): 三角形

    Returns:
        Point: 三角形 T の垂心
    """

    return T.A+T.B+T.C-2*CircumCenter(T)

def Excenter(T: Triangle) -> tuple[Point, Point, Point]:
    """ 三角形 T の傍心 (3 個) を求める

    Args:
        T (Triangle): 三角形

    Returns:
        tuple[Point, Point, Point]: 三角形 T の垂心 3個のタプル
    """

    a,b,c=T.three_edges()
    Ea=(-a*T.A+b*T.B+c*T.C)/(-a+b+c)
    Eb=(a*T.A-b*T.B+c*T.C)/(a-b+c)
    Ec=(a*T.A+b*T.B-c*T.C)/(a+b-c)
    return (Ea, Eb, Ec)

#=== 三角形の形状
def is_Acute_Triangle(T: Triangle) -> bool:
    """ 三角形 T が鋭角三角形かどうかを判定する.

    Args:
        T (Triangle): 三角形

    Returns:
        bool: 鋭角三角形 ?
    """

    a, b, c =  T.three_edges()
    m = max(a, b, c)
    return compare(a * a + b * b + c * c, 2 * m * m) == 1

def is_Right_Triangle(T: Triangle) -> bool:
    """ 三角形 T が直角三角形かどうかを判定する.

    Args:
        T (Triangle): 三角形

    Returns:
        bool: 直角三角形 ?
    """

    a, b, c =  T.three_edges()
    m = max(a, b, c)
    return compare(a * a + b * b + c * c, 2 * m * m) == 0

def is_Obtuse_Triangle(T: Triangle) -> bool:
    """ 三角形 T が鈍角三角形かどうかを判定する.

    Args:
        T (Triangle): 三角形

    Returns:
        bool: 鈍角三角形 ?
    """

    a, b, c =  T.three_edges()
    m = max(a, b, c)
    return compare(a * a + b * b + c * c, 2 * m * m) == -1

def Triangle_Division_by_Angle(T: Triangle) -> int:
    """ 三角形 T の形状を求める

    Args:
        T (Triangle): 三角形

    Returns:
        int:
            1: 鋭角三角形
            0: 直角三角形
            -1: 鈍角三角形
    """

    a, b, c =  T.three_edges()
    m = max(a, b, c)
    return compare(a * a + b * b + c * c, 2 * m * m)

def is_Isosceles_Triangle(T: Triangle) -> bool:
    """ 三角形 T が二等辺三角形かどうかを判定する.

    Args:
        T (Triangle): 三角形

    Returns:
        bool: 二等辺三角形 ?
    """

    a, b, c = T.three_edges()
    return (compare(a,b) == 0) or (compare(b, c) == 0) or (compare(c, a) == 0)

def is_Isosceles_Right_Triangle(T: Triangle) -> bool:
    """ 三角形 T が直角二等辺三角形かどうかを判定する.

    Args:
        T (Triangle): 三角形

    Returns:
        bool: 直角二等辺三角形 ?
    """

    return is_Right_Triangle(T) and is_Isosceles_Triangle(T)


def is_Equilateral_Triangle(T: Triangle) -> bool:
    """ 三角形 T が正三角形かどうかを判定する.

    Args:
        T (Triangle): 三角形

    Returns:
        bool: 正三角形 ?
    """

    a, b, c = T.three_edges()
    return compare(a,b) == 0 and compare(b, c) == 0 and compare(c, a) == 0

#=== 三角形の決定
def SSS_Triangle(a: float, b: float, c: float) -> Triangle:
    """ 3 辺の長さが a, b, c である三角形を生成する.

    Args:
        a (float): 辺 BC の長さ
        b (float): 辺 CA の長さ
        c (float): 辺 AB の長さ

    Raises:
        ValueError: a + b < c, b + c < a, c + a < b を満たしていなければならない.

    Returns:
        Triangle: 3 辺の長さが a, b, c である三角形を生成する.
    """

    if compare(2 * max(a, b, c), a + b + c) == -1:
        raise ValueError

    t=a+b+c

    A = Point()
    B = Point(c, 0)

    x = (- a * a + b * b + c * c) / (2 * c)
    y = sqrt(t * (t - 2 * a) * (t - 2 * b) * (t - 2  *c)) / (2 * c)
    C = Point(x, y)
    return Triangle(A, B, C)

def SAS_Triangle(a: float, gamma: float, b: float) -> Triangle:
    """ 2 辺の長さが a,b で, その間の角度が gamma である三角形を生成する.

    Args:
        a (float): 辺 BC の長さ
        gamma (float): 角 C の大きさ
        b (float): 辺 CA の長さ

    Raises:
        ValueError: 0 <= gamma <= pi でなくてはならない.

    Returns:
        Triangle: 2 辺の長さが a,b で, その間の角度が gamma である三角形
    """

    if not(0 <= gamma <= pi):
        raise ValueError

    t = sqrt(a * a + b * b - 2 * a * b * cos(gamma))

    A = Point()
    B = Point(t,0)
    C = Point((b * b- a * b * cos(gamma)) / t, (a * b * sin(gamma)) / t)
    return Triangle(A, B, C)

def ASA_Triangle(alpha: float, c: float, beta: float) -> Triangle:
    """ 1 辺の長さが c で, 両端の角度が alpha, beta である三角形を生成する

    Args:
        alpha (float): 角 A の大きさ
        c (float): 辺 AB の長さ
        beta (float): 角 B の大きさ

    Raises:
        ValueError: alpha + beta <= pi でなくてはならない.

    Returns:
        Triangle: 1 辺の長さが c で, 両端の角度が alpha, beta である三角形
    """

    if not alpha + beta <= pi:
        raise ValueError

    t = sin(beta) / sin(alpha + beta)

    A = Point()
    B = Point(c, 0)
    C = Point(c * t * cos(alpha), c * t * sin(alpha))
    return Triangle(A, B, C)

def AAS_Triangle(alpha: float, beta: float, a: float) -> Triangle:
    """ 1 辺の長さが a で, 2つの角が alpha, beta である三角形を生成する (a の対角が alpha).

    Args:
        alpha (float): 角 A の大きさ
        beta (float): 角 B の大きさ
        a (float): 辺 BC の長さ

    Raises:
        ValueError: alpha + beta <= pi でなくてはならない.

    Returns:
        Triangle: 1 辺の長さが a で, 2つの角が alpha, beta である三角形
    """
    if alpha + beta <= pi:
        raise ValueError

    A = Point()
    B = Point(a * sin(alpha + beta) / sin(alpha), 0)
    C = Point(a * sin(beta) * cos(alpha) / sin(alpha), a * sin(beta))
    return Triangle(A, B, C)
