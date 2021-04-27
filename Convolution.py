def FFT(A,inverse=False):
    from math import sin,cos,exp,pi

    n=len(A)
    max_level=(n-1).bit_length()
    m=1<<max_level

    w=complex(cos(2*pi/m),sin(2*pi/m))

    if inverse: #逆変換ならば...
        w=1/w #逆元

    W=[0]*(max_level+1)
    W[-1]=w

    for k in range(max_level-1,-1,-1):
        W[k]=W[k+1]*W[k+1]

    U=[[0]*(1<<x) for x in range(max_level+1)]

    for y in range(1,max_level+1):
        for x in range(1<<y):
            if x==0:
                U[y][x]=1
            else:
                U[y][x]=U[y][x-1]*W[y]

    def fft(x,level):
        t=len(x)
        if t==1:
            return x

        y=[0]*(t>>1)
        z=[0]*(t>>1)

        for k in range(t//2):
            y[k]=x[k]+x[k+t//2]
            z[k]=(x[k]-x[k+t//2])*U[level][k]

        y=fft(y,level-1)
        z=fft(z,level-1)

        x=[0]*t
        for k in range(t>>1):
            x[2*k]=y[k]
            x[2*k+1]=z[k]

        return x

    B=A+[0]*(m-n)
    return fft(B,max_level)

def Inverse_FFT(A):
    G=FFT(A,True)
    return [a/len(G) for a in G]

def Convolution(A,B):
    from math import floor

    N=len(A);M=len(B)
    if N==0 or M==0:
        return []

    z=1<<((N+M-2).bit_length())

    A=A+[0]*(z-N)
    B=B+[0]*(z-M)

    P=FFT(A)
    Q=FFT(B)

    R=[0]*z
    for i in range(z):
        R[i]=P[i]*Q[i]
    R=Inverse_FFT(R)
    return  [floor(a.real+1/2) for a in R]

#=================================================
def Primitive_Root(p):
    if p==2:
        return 1

    fac=[]
    q=2
    v=p-1

    while v>=q*q:
        e=0
        while v%q==0:
            e+=1
            v//=q

        if e>0:
            fac.append(q)
        q+=1

    if v>1:
        fac.append(v)

    g=2
    while g<p:
        if pow(g,p-1,p)!=1:
            return None

        flag=True
        for q in fac:
            if pow(g,(p-1)//q,p)==1:
                flag=False
                break

        if flag:
            return g

        g+=1

def NTT(A,Mod,primitive=None,inverse=False):
    n=len(A)
    max_level=(n-1).bit_length()
    m=1<<max_level

    if primitive==None:
        primitive=Primitive_Root(Mod)

    u=Mod-1
    e=0
    while u%2==0:
        e+=1
        u>>=1

    w=pow(primitive,u,Mod)

    if inverse: #逆変換ならば...
        w=pow(w,Mod-2,Mod) #逆元

    W=[0]*(e+1)
    W[-1]=w

    for k in range(e-1,-1,-1):
        W[k]=(W[k+1]*W[k+1])%Mod

    U=[[0]*(1<<x) for x in range(max_level+1)]

    for y in range(1,max_level+1):
        for x in range(1<<y):
            if x==0:
                U[y][x]=1
            else:
                U[y][x]=(U[y][x-1]*W[y])%Mod

    def ntt(x,level):
        t=len(x)
        if t==1:
            return x

        y=[0]*(t>>1)
        z=[0]*(t>>1)

        for k in range(t//2):
            y[k]=(x[k]+x[k+t//2])%Mod
            z[k]=((x[k]-x[k+t//2])*U[level][k])%Mod

        y=ntt(y,level-1)
        z=ntt(z,level-1)

        x=[0]*t
        for k in range(t>>1):
            x[2*k]=y[k]
            x[2*k+1]=z[k]

        return x

    B=A+[0]*(m-n)
    return ntt(B,max_level)

def Inverse_NTT(A,Mod,primitive=None):
    B=NTT(A,Mod,primitive,inverse=True)
    N_inv=pow(len(A),Mod-2,Mod)
    return [(N_inv*b)%Mod for b in B]

def Convolution_Mod(A,B,Mod,primitive=None):
    N=len(A);M=len(B)
    if N==0 or M==0:
        return []

    z=1<<((N+M-2).bit_length())

    A=A+[0]*(z-N)
    B=B+[0]*(z-M)

    if primitive==None:
        primitive=Primitive_Root(Mod)

    P=NTT(A,Mod,primitive)
    Q=NTT(B,Mod,primitive)

    R=[(P[i]*Q[i])%Mod for i in range(z)]

    return Inverse_NTT(R,Mod,primitive)
#=================================================
