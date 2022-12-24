def Largest_Rectangle(H, mode=0):
    """ ヒストグラム H における最大長方形のサイズを求める.

    H: リスト
    mode: 1 のときはその範囲も求める.
    """
    from collections import deque
    H=H+[0]
    S=deque([])
    X=H[0]
    l=r=-1
    for i in range(len(H)):
        if (not S) or H[S[-1]]<H[i]:
            S.append(i)
        else:
            while S and H[S[-1]]>=H[i]:
                j=S.pop()
                if X<H[j]*(i-j):
                    X=H[j]*(i-j)
                    l=j; r=i-1
            H[j]=H[i]
            S.append(j)

    if mode==0:
        return X
    else:
        return X,(l,r)
