#Z-Algorithm
def Z_Algorithm(S):
    """ i=0,1,...,|S|-1 に対して, S[i...] と S の先頭何文字が一致しているかを表すリストを返す.

    S: string
    """
    N=len(S)
    Z=[0]*N
    i,j=1,0
    Z[0]=N
    while i<N:
        while i+j <N and S[j] == S[i+j]:
            j+=1

        if not j:
            i+=1
            continue

        Z[i] = j
        k = 1
        while N-i>k<j-Z[k]:
            Z[i+k]=Z[k]
            k+=1
        i+=k
        j-=k
    return Z
