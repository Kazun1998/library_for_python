def Suffix_Array(S, encoder=lambda x:x):
    """ 文字列 S の Suffix Array (接尾辞配列) (S[0...], S[1...],... を辞書式に並べた時の開始インデックスの列) を SA-IS によって求める.

    S: 列
    encoder: 正の整数への順序埋め込み (※ max encoder(S) が小さいほど計算量がよい)
    """

    A=[encoder(x) for x in S]+[0]
    assert min(A[:-1])>0,"encoder の値域が正から外れています"
    k=max(A)+1
    n=len(A)

    def induce_l(sa, a, n, k, stype):
        bucket = get_buckets(a, k, 1)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not stype[j]):
                sa[bucket[a[j]]] = j
                bucket[a[j]] += 1

    def induce_s(sa, a, n, k, stype):
        bucket = get_buckets(a, k, 0)
        for i in range(n)[::-1]:
            j = sa[i] - 1
            if j >= 0 and stype[j]:
                bucket[a[j]] -= 1
                sa[bucket[a[j]]] = j

    def get_buckets(a, k, start = 0):
        bucket = [0] * k
        for item in a:
            bucket[item] += 1
        s = 0
        for i in range(k):
            s += bucket[i]
            bucket[i] = s - (bucket[i] if start else 0)
        return bucket

    def set_lms(a, n, k, default_order):
        bucket = get_buckets(a, k)
        sa = [-1] * n
        for i in default_order[::-1]:
            bucket[a[i]] -= 1
            sa[bucket[a[i]]] = i
        return sa

    def induce(a, n, k, stype, default_order):
        sa = set_lms(a, n, k, default_order)
        induce_l(sa, a, n, k, stype)
        induce_s(sa, a, n, k, stype)
        return sa

    def rename_LMS_substring(sa, a, n, stype, LMS, l):
        sa = [_s for _s in sa if LMS[_s]]
        tmp = [-1] * (n//2) + [0]
        dupl = 0
        for _ in range(1, l):
            i, j = sa[_-1], sa[_]
            for ii in range(n):
                if a[i+ii] != a[j+ii] or stype[i+ii] != stype[j+ii]:
                    break
                if ii and (LMS[i+ii] or LMS[j+ii]):
                    dupl += 1
                    break
            tmp[j//2] = _ - dupl
        tmp = [t for t in tmp if t >= 0]
        return tmp, dupl

    def calc(a, n, k):
        stype = [1] * n
        for i in range(n-1)[::-1]:
            if a[i] > a[i+1] or (a[i] == a[i+1] and stype[i+1] == 0):
                stype[i] = 0

        LMS = [1 if stype[i] and not stype[i-1] else 0 for i in range(n-1)] + [1]
        l = sum(LMS)
        lms = [i for i in range(n) if LMS[i]]
        sa = induce(a, n, k, stype, lms)
        renamed_LMS, dupl = rename_LMS_substring(sa, a, n, stype, LMS, l)

        if dupl:
            sub_sa = calc(renamed_LMS, l, l - dupl)
        else:
            sub_sa = [0] * l
            for i in range(l):
                sub_sa[renamed_LMS[i]] = i

        lms = [lms[sub_sa[i]] for i in range(l)]
        sa = induce(a, n, k, stype, lms)
        return sa

    return calc(A,n,k)[1:]

def Longest_Commom_Prefix(S, encoder=lambda x:x, with_SA=False):
    SA=Suffix_Array(S,encoder)
    N=len(S)
    rank=[0]*N

    for i in range(N):
        rank[SA[i]] = i

    LCP=[0]*(N - 1)
    h=0
    for i in range(N):
        if h: h -= 1
        if rank[i] == 0: continue
        j = SA[rank[i] - 1]
        while j + h < N and i + h < N:
            if S[j+h] != S[i+h]: break
            h += 1
        LCP[rank[i] - 1] = h

    if with_SA:
        return SA,LCP
    else:
        return LCP
