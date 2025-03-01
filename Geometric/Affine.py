from Point import *
from Line import *
from Circle import *
from Triangle import *
from Polygon import *

class Affine:
    __slots__ = ('mat', 'vec')

    def __init__(self, mat: list[list[float]] = None, vec: list[float] = None):
        if mat is None:
            mat = [[1, 0], [0, 1]]

        if vec is None:
            vec = [0, 0]

        self.mat = mat
        self.vec = vec

    def __str__(self) -> str:
        return f"Matrix: {self.mat}, Vector: {self.vec}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.mat}, {self.vec})"

    def __iter__(self):
        yield self.mat
        yield self.vec

    def __pos__(self) -> "Affine":
        return self

    def __neg__(self):
        [[a,b],[c,d]], [x, y] = self
        return Affine([[-a, -b], [-c, -d]], [-x, -y])

    def __add__(self, other):
        a = self.mat[0][0] + other.mat[0][0]
        b = self.mat[0][1] + other.mat[0][1]
        c = self.mat[1][0] + other.mat[1][0]
        d = self.mat[1][1] + other.mat[1][1]

        u = self.vec[0] + other.vec[1]
        v = self.vec[1] + other.vec[1]

        return Affine([[a, b], [c, d]], [u, v])

    def __sub__(self,other):
        a = self.mat[0][0] - other.mat[0][0]
        b = self.mat[0][1] - other.mat[0][1]
        c = self.mat[1][0] - other.mat[1][0]
        d = self.mat[1][1] - other.mat[1][1]

        u = self.vec[0] - other.vec[1]
        v = self.vec[1] - other.vec[1]

        return Affine([[a, b], [c, d]], [u, v])

    def __mul__(self, other):
        a = self.mat[0][0] * other.mat[0][0] + self.mat[0][1] * other.mat[1][0]
        b = self.mat[0][0] * other.mat[0][1] + self.mat[0][1] * other.mat[1][1]
        c = self.mat[1][0] * other.mat[0][0] + self.mat[1][1] * other.mat[1][0]
        d = self.mat[1][0] * other.mat[0][1] + self.mat[1][1] * other.mat[1][1]

        u = self.mat[0][0] * other.vec[0] + self.mat[0][1] * other.vec[1] + self.vec[0]
        v = self.mat[1][0] * other.vec[0] + self.mat[1][1] * other.vec[1] + self.vec[1]

        return Affine([[a, b], [c, d]], [u, v])

    def __pow__(self, n):
        if n < 0:
            return pow(self, -n).inverse()

        A = self
        B = Affine()
        while n:
            if n & 1:
                B *= A
            n >>= 1
            A *= A
        return  B

    def __eq__(self, other):
        return self.mat == other.mat and self.vec == other.vec

    def inverse(self) -> "Affine":
        [[a, b], [c, d]], [x, y] = self

        det = a * d - b * c
        p, q, r, s = d / det, -b / det, -c / det, a/ det
        return Affine([[p, q], [r, s]], [-(p * x  + q * y), -(r * x + s * y)])

    def integerization(self, delta = 1e-7):
        for i in [0, 1]:
            for j in [0, 1]:
                if abs(self.mat[i][j] - floor(self.mat[i][j] + 0.5)) < delta:
                    self.mat[i][j] = floor(self.mat[i][j] + 0.5)

        if abs(self.vec[0] - floor(self.vec[0] + 0.5)) < delta:
            self.vec[0] = floor(self.vec[0] + 0.5)

        if abs(self.vec[1] - floor(self.vec[1] + 0.5)) < delta:
            self.vec[1] = floor(self.vec[1] + 0.5)

    def __getitem__(self, shape):
        return Action(self, shape)

#=== 作用
def Action(A: Affine, S):
    """ 図形 S にアフィン変換 A を施した後の結果を返す.

    Args:
        A (Affine): アフィン変換
        S : 図形

    Raises:
        NotImplemented: アフィン変換で円が円に映るとは限らない (一般には楕円)

    Returns: アフィン変換後の図形
    """

    if isinstance(S, Point):
        [[a, b], [c, d]], [x, y] = A
        return Point(a * S.x + b * S.y + x, c * S.x + d * S.y + y)
    elif isinstance(S, Segment):
        return Segment(Action(A, S.begin), Action(A, S.end))
    elif isinstance(S, Ray):
        return Ray(Action(A, S.begin), Action(A, S.end))
    elif isinstance(S, Line):
        return Line(Action(A, S.begin), Action(A, S.end))
    elif isinstance(S, Circle):
        raise NotImplemented
    elif isinstance(S, Triangle):
        return Triangle(Action(A, S.A), Action(A, S.B), Action(A, S.C))
    elif isinstance(S, Polygon):
        return Polygon(*[Action(A, P) for P in S.vertices])

#=== アフィン変換の生成
def Translation(x: float, y: float) -> Affine:
    """ (x, y) だけ平行移動させるアフィン変換を求める.

    Args:
        x (float): x 座標の移動量
        y (float): y 座標の移動量

    Returns:
        Affine: (x, y) だけ平行移動させるアフィン変換
    """
    return Affine(vec=[x, y])

def Point_Reflection(x: float = 0, y: float = 0) -> Affine:
    """ 点 (x,y) に関する対称移動をするアフィン変換を生成する.

    Args:
        x (float, optional): 点の x 座標. Defaults to 0.
        y (float, optional): 点の y 座標. Defaults to 0.

    Returns:
        Affine: 点 (x,y) に関する対称移動をするアフィン変換
    """

    return Affine([[-1, 0], [0, -1]], [2 * x, 2 * y])

def Line_Reflection(a: float, b: float, c: float) -> Affine:
    """ 直線 a x + b y + c = 0 に関する対称移動をするアフィン変換を生成する.

    Args:
        a (float):
        b (float):
        c (float):

    Raises:
        ValueError: a = b = 0 のときに発生

    Returns:
        Affine: 直線 a x + b y + c = 0 に関する対称移動
    """
    if (sign(a) == 0) or (sign(b) == 0):
        raise ValueError

    k = a * a + b * b

    p = (- a * a + b * b) / k
    q = - 2 * a * b / k
    r = - 2 * c / k

    return Affine([[p, q], [q, -p]], [a * r , b * r])

def Rotation(theta: float, x: float = 0, y: float = 0) -> Affine:
    """ 点 (x, y) 周りで theta (時計回り) に回転させるアフィン変換を生成する.

    Args:
        theta (float): 回転角
        x (float, optional): 中心となる点の x 座標. Defaults to 0.
        y (float, optional): 中心となる点の y 座標. Defaults to 0.

    Returns:
        Affine: 点 (x, y) 周りで theta (時計回り) に回転させるアフィン変換
    """

    c = cos(theta); s = sin(theta)
    return Affine([[c, -s], [s, c]], [(1 - c) * x + s * y, -s * x + (1 - c) * y])

#=== アフィン変換の決定
def Translation_and_Rotate_Affine_Determine(A: Point, B: Point, P: Point, Q: Point) -> Affine:
    """ 平行移動と回転のみによって生成され F(A) = P, F(B) = Q を満たすアフィン変換を求める.

    Args:
        A (Point):
        B (Point):
        P (Point): F(A)
        Q (Point): F(B)

    Raises:
        ValueError: |AB| = |PQ| でなくてはならない.

    Returns:
        Affine: 平行移動と回転のみによって生成され F(A) = P, F(B) = Q を満たす
    """

    if compare(abs(B - A), abs(Q - P)):
        raise ValueError

    return Rotation(Arg(Q, P) - Arg(B, A), *P) * Translation(*(P-A))

def Affine_Determine(A: Point, B: Point, C: Point, P: Point, Q: Point, R: Point) -> Affine:
    """ 平行移動と回転のみによって生成され F(A) = P, F(B) = Q, F(C) = R を満たすアフィン変換を求める.

    Args:
        A (Point):
        B (Point):
        C (Point):
        P (Point): F(A)
        Q (Point): F(B)
        R (Point): F(C)

    Raises:
        ValueError: A, B, C は同一直線上の 3 点であってはいけない.

    Returns:
        Affine: 平行移動と回転のみによって生成され F(A) = P, F(B) = Q, F(C) = R を満たすアフィン変換
    """

    if compare((B - A).det(C - A)) == 0:
        raise ValueError

    q1, q2 = Q - P
    r1, r2 = R - P
    b1, b2 = B - A
    c1, c2 = C - A
    det = b1 * c2 - b2 * c1

    M = [
            [(q1 * c2 - r1 * b2) / det, (-q1 * c1 + r1 * b1) / det],
            [(q2 *c2 - r2 * b2) / det, (-q2 * c1 + r2 * b1) / det]
        ]

    v = [
            P.x - (M[0][0] * A.x + M[0][1] * A.y),
            P.y - (M[1][0] * A.x + M[1][1] * A.y)
        ]

    return Affine(M, v)
