# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear

#==================================================
from Summation.Floor_Sum import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    T=int(input())

    Ans=[0]*T
    for t in range(T):
        N,M,A,B=map(int,input().split())
        Ans[t]=floor_sum(A,B,M,N)

    write("\n".join(map(str,Ans)))

#==================================================
verify()