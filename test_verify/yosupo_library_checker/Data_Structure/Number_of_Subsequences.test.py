# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_subsequences

#==================================================
from Sequence.Subsequence_Count import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=list(map(int,input().split()))

    Mod=998244353
    print(Subsequence_Count(A, Mod, False))

#==================================================
verify()
