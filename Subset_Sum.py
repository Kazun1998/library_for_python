def Subset_Sum_Zero_One(A, S, Mod=None, mode=False):
    """ A の多重部分集合で, 和が S になる数を求める.

    Mod: 余り
    mode: True ならば 0,1,2,...,S の場合全て, false ならば S のみ

    計算量: O(|A| S)
    """

    DP=[0]*(S+1); DP[0]=1
    T=0

    for a in A:
        T+=a
        for x in range(min(S,T),a-1,-1):
            DP[x]+=DP[x-a]

        if Mod!=None:
            for i in range(a,min(S,T)+1):
                DP[i]%=Mod

    if mode:
        return DP
    else:
        return DP[S]

def Subset_Sum_Plus_Minus_One(A, K, Mod=None):
    """ 以下を満たす A の分割 X,Y の個数を求める: sum(X)-sum(Y)=K.

    計算量: O(N(sum(A)+K))
    """

    L=K+sum(abs(a) for a in A)
    if L<0 or L%2==1:
        return 0

    B=[abs(a) for a in A]
    return Subset_Sum_Zero_One(B, L//2, Mod)
