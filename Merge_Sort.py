def Merge_Sort_by_Index(X):
    """ マージソートする (返り値は添字).

    X: リスト
    """

    def merge(left, mid, right):
        i=left; j=mid; k=0

        J=[0]*(right-left)
        while (i<mid and j<right):
            if X[I[i]]<X[I[j]]:
                J[k]=I[i]
                i+=1
            else:
                J[k]=I[j]
                j+=1
            k+=1

        if i==mid:
            J[k:]=I[j:right]
        else:
            J[k:]=I[i:mid]

        I[left:right]=J

    def sort(left, right):
        if right-left<=1:
            return

        mid=(left+right)//2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    N=len(X)
    I=list(range(N))
    sort(0,N)
    return I

def Merge_Sort(X):
    """ マージソートする.

    X: リスト
    """

    return [X[i] for i in Merge_Sort_by_Index(X)]
