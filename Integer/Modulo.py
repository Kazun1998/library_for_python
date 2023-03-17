#法 p の原始根
def Primitive_Root(p):
    """Z/pZ上の原始根を見つける

    p:素数
    """
    if p==2:
        return 1
    if p==998244353:
        return 3
    if p==10**9+7:
        return 5

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

#拡張ユークリッドの互除法
def Extend_Euclid(a: int, b: int):
    """ gcd(a,b) と ax+by=gcd(a,b) を満たす整数 x,y の例を挙げる.

    [Input]
    a,b: 整数

    [Output]
    (x,y,gcd(a,b))
    """
    s,t,u,v=1,0,0,1
    while b:
        q,a,b=a//b,b,a%b
        s,t=t,s-q*t
        u,v=v,u-q*v
    return s,u,a


def Modulo_Inverse(a, m):
    """ (mod m) における逆元を求める.

    Args:
        a (int): mod m の元
        m (int): 法

    Returns:
        int: 可逆元が存在するならばその値, 存在しないのであれば -1
    """

    h=Extend_Euclid(a,m)
    return h[0]%m if h[2]==1 else -1

