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
 
def Arg(P,Q=Point(0,0)):
    """点 Q から見た点 P の偏角を求める.
 
    P,Q: Point
    """
 
    R=Q-P
    return atan2(R.y,R.x)
 
def Action(A: Affine,S):
    """ アフィン変換 A に図形 S を作用させる.
 
    A: Affine
    S: 図形 (Point, Line_Segment, Triangle)
    """
 
    if isinstance(S,Point):
        [[a,b],[c,d]]=A.Mat
        u,v=A.Vec
        return Point(a*S.x+b*S.y+u, c*S.x+d*S.y+v)
    elif isinstance(S,Line_Segment):
        return Line_Segment(Action(A,S.P), Action(A,S.Q))
    elif isinstance(S,Triangle):
        return Triangle(Action(A,S.A), Action(A,S.B), Action(A,S.C))
 
def Translation(x,y):
    """ (x,y) だけ平行移動させるアフィン変換を生成する.
    """
 
    return Affine(Vec=[x,y])
 
def Rotation(theta,Px=0,Py=0):
    """ 点 P=(Px,Py) 周りで theta (時計回り) に回転させるアフィン変換を生成する.
    """
    c=cos(theta); s=sin(theta)
    return Affine([[c,-s],[s,c]], [(1-c)*Px+s*Py,-s*Px+(1-c)*Py])
