from Point import *
from Line import *
from Circle import *
from Triangle import *
from Polygon import *

class Affine():
    def __init__(self,Mat=[[1,0],[0,1]],Vec=[0,0]):
        self.Mat=Mat
        self.Vec=Vec

    def __str__(self):
        return "Mat: {}, Vec:{}".format(self.Mat,self.Vec)

    __repr__=__str__

    def __pos__(self):
        return self

    def __neg__(self):
        [[a,b],[c,d]]=self.Mat
        x,y=self.Vec
        return Affine([[-a,-b],[-c,-d]],[-x,-y])

    def __add__(self,other):
        M=[[0,0],[0,0]]
        M[0][0]=self.Mat[0][0]+other.Mat[0][0]
        M[0][1]=self.Mat[0][1]+other.Mat[0][1]
        M[1][0]=self.Mat[1][0]+other.Mat[1][0]
        M[1][1]=self.Mat[1][1]+other.Mat[1][1]

        v=[self.Vec[0]+other.Vec[0], self.Vec[1]+other.Vec[1]]

        return Affine(M,v)

    def __sub__(self,other):
        M=[[0,0],[0,0]]
        M[0][0]=self.Mat[0][0]-other.Mat[0][0]
        M[0][1]=self.Mat[0][1]-other.Mat[0][1]
        M[1][0]=self.Mat[1][0]-other.Mat[1][0]
        M[1][1]=self.Mat[1][1]-other.Mat[1][1]

        v=[self.Vec[0]-other.Vec[0], self.Vec[1]-other.Vec[1]]

        return Affine(M,v)

    def __mul__(self,other):
        M=[[0,0],[0,0]]
        M[0][0]=self.Mat[0][0]*other.Mat[0][0]+self.Mat[0][1]*other.Mat[1][0]
        M[0][1]=self.Mat[0][0]*other.Mat[0][1]+self.Mat[0][1]*other.Mat[1][1]
        M[1][0]=self.Mat[1][0]*other.Mat[0][0]+self.Mat[1][1]*other.Mat[1][0]
        M[1][1]=self.Mat[1][0]*other.Mat[0][1]+self.Mat[1][1]*other.Mat[1][1]

        v=[
            self.Mat[0][0]*other.Vec[0]+self.Mat[0][1]*other.Vec[1]+self.Vec[0],
            self.Mat[1][0]*other.Vec[0]+self.Mat[1][1]*other.Vec[1]+self.Vec[1]
            ]
        return Affine(M,v)

    def __pow__(self,n):
        if n<0:
            return pow(self,-n).inverse()

        A=self
        B=Affine()
        while n:
            if n&1:
                B*=A
            n>>=1
            A*=A
        return  B

    def __eq__(self,other):
        return self.Mat==other.Mat and self.Vec==other.Vec

    def inverse(self):
        [[a,b],[c,d]]=self.Mat
        x,y=self.Vec

        det=a*d-b*c
        p,q,r,s=d/det,-b/det,-c/det,a/det
        return Affine([[p,q],[r,s]],[-(p*x+q*y), -(r*x+s*y)])

    def integerization(self,delta=1e-7):
        for i in [0,1]:
            for j in [0,1]:
                if abs(self.Mat[i][j]-floor(self.Mat[i][j]+0.5))<delta:
                    self.Mat[i][j]=floor(self.Mat[i][j]+0.5)

        if abs(self.Vec[0]-floor(self.Vec[0]+0.5))<delta:
            self.Vec[0]=floor(self.Vec[0]+0.5)

        if abs(self.Vec[1]-floor(self.Vec[1]+0.5))<delta:
            self.Vec[1]=floor(self.Vec[1]+0.5)

    def __getitem__(self,shape):
        return Action(self,shape)

#=== 作用
def Action(A: Affine,S):
    """ アフィン変換 A に図形 S を作用させる.

    A: Affine
    S: 図形 (Point, Line_Segment, Triangle)
    """

    if isinstance(S,Point):
        [[a,b],[c,d]]=A.Mat
        u,v=A.Vec
        return Point(a*S.x+b*S.y+u, c*S.x+d*S.y+v)
    elif isinstance(S,Segment):
        return Segment(Action(A,S.begin),Action(A,S.end))
    elif isinstance(S,Ray):
        return Ray(Action(A,S.begin),Action(A,S.end))
    elif isinstance(S,Line):
        return Line(Action(A,S.begin),Action(A,S.end))
    elif isinstance(S,Circle):
        pass
    elif isinstance(S,Triangle):
        return Triangle(Action(A,S.A), Action(A,S.B), Action(A,S.C))
    elif isinstance(S,Polygon):
        return Polygon(*[Action(A,p) for p in S.vertices])

#=== アフィン変換の生成
def Translation(x,y):
    """ (x,y) だけ平行移動させるアフィン変換を生成する.
    """

    return Affine(Vec=[x,y])

def Point_Reflection(x=0,y=0):
    """ 点 (x,y) に関する対称移動をするアフィン変換を生成する.
    """

    return Affine([[-1,0],[0,-1]],[2*x,2*y])

def Line_Reflection(a,b,c):
    """ 直線 ax+by+c=0 に関する対称移動をするアフィン変換を生成する.
    """

    assert (a!=0) or (b!=0)

    k=a*a+b*b

    p=(-a*a+b*b)/k; q=-2*a*b/k; r=-2*c/k
    return Affine([[p,q],[q,-p]],[a*r,b*r])

def Rotation(theta,Px=0,Py=0):
    """ 点 P=(Px,Py) 周りで theta (時計回り) に回転させるアフィン変換を生成する.
    """
    c=cos(theta); s=sin(theta)
    return Affine([[c,-s],[s,c]], [(1-c)*Px+s*Py,-s*Px+(1-c)*Py])

#=== アフィン変換の決定
def Translation_and_Rotate_Affine_Determine(A,B,P,Q):
    """ F(A)=P, F(B)=Q となるアフィン変換 F のうち, 平行移動と回転で生成されるものを生成する.

    A,B,P,Q: Point
    ※ |AB|=|PQ| でなくてはならない.
    """

    assert abs(B-A)==abs(Q-P)


    return Rotation(Arg(Q,P)-Arg(B,A),*P)*Translation(*(P-A))

def Affine_Determine(A,B,C,P,Q,R):
    """ F(A)=P, F(B)=Q, F(C)=R となるアフィン変換 F を求める.

    A,B,C,P,Q,R: Point
    ※ A,B,C は同一直線上の点であってはいけない.
    """

    assert compare((B-A).det(C-A),0)

    q1,q2=Q-P; r1,r2=R-P
    b1,b2=B-A; c1,c2=C-A; det=b1*c2-b2*c1

    M=[
        [(q1*c2-r1*b2)/det, (-q1*c1+r1*b1)/det],
        [(q2*c2-r2*b2)/det, (-q2*c1+r2*b1)/det]
        ]

    v=[P.x-(M[0][0]*A.x+M[0][1]*A.y), P.y-(M[1][0]*A.x+M[1][1]*A.y)]

    return Affine(M,v)
