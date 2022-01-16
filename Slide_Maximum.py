from collections import deque

def Slide_Maximum_Index(A,k):
    """リストA の k 要素スライド最大値をもつインデックスを求める.

    [Input]
    A: List
    k: Length

    [Output]
    M: 長さ |A|-k+1 のリストで, 第 i 要素は max(A[i], ..., A[i+k-1])=A[M[i]] となるようになる.
    """

    N=len(A)
    index=[0]*N
    Q=deque()

    for i in range(N):
        while Q and Q[0]<=i-k:
            Q.popleft()

        while Q and A[Q[-1]]<A[i]:
            Q.pop()
        Q.append(i)
        index[i]=Q[0]
    return index

def Slide_Maximum_Value(A,k):
    """リストA の k 要素スライド最大値を求める.

    [Input]
    A: List
    k: Length

    [Output]
    M: 長さ |A|-k+1 のリストで, 第 i 要素は max(A[i], ..., A[i+k-1])=A[M[i]] となるようになる.
    """

    N=len(A)
    res=[0]*N
    Q=deque()

    for i in range(N):
        while Q and Q[0]<=i-k:
            Q.popleft()

        while Q and A[Q[-1]]<A[i]:
            Q.pop()
        Q.append(i)
        res[i]=A[Q[0]]
    return res
