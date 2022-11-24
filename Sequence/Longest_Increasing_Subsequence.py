def Longest_Increasing_Subsequence(A, mode=False, equal=False):
    """ 列 L における LIS の長さを求める.

    Mode=False のとき ... LIS の長さ, True のとき ... (長さ, 一例, 一例の各要素の場所)
    equal: False のとき ... 狭義単調増加, True のとき... 広義単調増加
    """

    if equal:
        from bisect import bisect_right as bis
    else:
        from bisect import bisect_left as bis

    if mode:
        L=[]
        Ind=[0]*len(A)
        for i in range(len(A)):
            a=A[i]
            k=bis(L,a)
            if k==len(L):
                L.append(a)
            else:
                L[k]=a
            Ind[i]=k

        X=[]
        I=[]
        j=len(L)-1
        for i in range(len(A)-1,-1,-1):
            if Ind[i]==j:
                j-=1
                X.append(A[i])
                I.append(i)

        return len(L), X[::-1], I[::-1]
    else:
        L=[]
        for a in A:
            k=bis(L,a)
            if k==len(L):
                L.append(a)
            else:
                L[k]=a
        return len(L)
