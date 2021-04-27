def Knapsack_01_Weight(List,Weight,Mode=False):
    """重さが非常に軽い01-Knapsack Problemを解く.

    List:各要素はタプル(v,w) の形で, vは価値, wは重さ
    Mode:Mode=Trueのとき, 最大値とそれを達成する例を返す.
    [計算量]
    O(NW)
    """

    if Mode:
        X=[[0]*(Weight+1) for _ in range(len(List)+1)]
        for i,(v,w) in enumerate(List,0):
            E=X[i]
            F=X[i+1]

            for s in range(Weight,w-1,-1):
                F[s]=max(E[s],E[s-w]+v)
        alpha=max(X[-1])
        W=X[-1].index(alpha)

        L=[]
        for i in range(len(List)-1,-1,-1):
            if X[i+1][W]>X[i][W]:
                v,w=List[i]
                L.append((i,List[i]))
                W-=w
        return alpha,L[::-1]
    else:
        X=[0]*(Weight+1)
        for v,w in List:
            for s in range(Weight,w-1,-1):
                X[s]=max(X[s],X[s-w]+v)
        return max(X)

def Knapsack_01_Value(List,Weight,Mode=False):
    """価値が非常に小さい01-Knapsack Problemを解く.

    List:各要素はタプル(v,w) の形で, vは価値, wは重さ
    Mode:Mode=Trueのとき, 最大値とそれを達成する例を返す.
    [計算量]
    O(N sum(v))
    """

    inf=float("inf")
    v_sum=0
    for v,_ in List:
        v_sum+=v

    if Mode:
        X=[[inf]*(v_sum+1) for _ in range(len(List)+1)]
        X[0][0]=0

        for i,(v,w) in enumerate(List,0):
            E=X[i]
            F=X[i+1]

            for s in range(v_sum,v-1,-1):
                F[s]=min(E[s],E[s-v]+w)
            for s in range(v-1,-1,-1):
                F[s]=E[s]

        E=X[-1]
        Y=[v for v in range(v_sum+1) if E[v]<=Weight]
        V=alpha=max(Y)

        L=[]
        for i in range(len(List)-1,-1,-1):
            if X[i+1][V]<X[i][V]:
                v,w=List[i]
                L.append((i,List[i]))
                V-=v
        return alpha,L[::-1]
    else:
        X=[inf]*(v_sum+1)
        X[0]=0

        for v,w in List:
            for s in range(v_sum,v-1,-1):
                X[s]=min(X[s],X[s-v]+w)
        Y=[v for v in range(v_sum+1) if X[v]<=Weight]
        return max(Y)

def Knapsack_01_Middle(List,Weight,Mode=False):
    """個数が非常に少ない01-Knapsack Problemを (半分全列挙で) 解く.

    List:各要素はタプル(v,w) の形で, vは価値, wは重さ
    [計算量]
    O(N 2^(N/2))

    [参考元]
    https://tjkendev.github.io/procon-library/python/dp/knapsack-meet-in-the-middle.html
    """

    def subset_sum(S):
        T={0:0}
        for v,w in S:
            T1=dict(T)
            for key,val in T.items():
                a=key+w
                if a>Weight:
                    continue
                if a in T1:
                    T1[a]=max(T1[a],val + v)
                else:
                    T1[a]=val+v
            T=T1

        v=-1
        R=[]
        for w in sorted(T):
            if T[w]>v:
                v=T[w]
                R.append((v,w))
        return R

    def merge(S,T):
        T=T[::-1]
        it=iter(T)
        v1,w1=next(it)

        t=0

        for v,w in S:
            while w+w1>Weight:
                v1,w1=next(it)

            if t<v+v1:
                t=v+v1
        return t

    N=len(List)
    A=subset_sum(List[:N//2])
    B=subset_sum(List[N//2:])
    return merge(A,B)
