# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod

#==================================================
from Sequence.Longest_Increasing_Subsequence import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=list(map(int,input().split()))

    K,_,I=Longest_Increasing_Subsequence(A, mode=True, equal=False)

    print(K)
    write(" ".join(map(str,I)))


#==================================================
verify()
