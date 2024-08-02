# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree

#==================================================
from Sequence.Cartesian_Tree import Cartesian_Tree

import sys
input=sys.stdin.readline
write=sys.stdout.write
#==================================================
def verify():
    N = int(input())
    A = list(map(int, input().split()))
    print(*[t if t != -1 else i for i, t in enumerate(Cartesian_Tree(A).parent)])


#==================================================
verify()
