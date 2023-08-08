# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_point_get

#==================================================
import sys
from  Segment_Tree.Dual_Segment_Tree import Dual_Segment_Tree

input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    def comp(g, f):
        f0 = f >> bit; f1 = f & msk
        g0 = g >> bit; g1 = g & msk

        h0 = (g0 + g1 * f0) % Mod
        h1 = (f1 * g1) % Mod
        return (h0 << bit) + h1

    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    Mod = 998244353
    bit = 32; msk =(1 << bit) - 1
    D = Dual_Segment_Tree([a << bit for a in A], comp, 1)

    Ans=[]
    for q in range(Q):
        mode, *query = map(int, input().split())
        if mode == 0:
            l, r, b, c = query
            D.action(l, r, (c << bit) + b, True, False)
        else:
            Ans.append(D[query[0]] >> bit)

    write("\n".join(map(str, Ans)))

#==================================================
verify()
