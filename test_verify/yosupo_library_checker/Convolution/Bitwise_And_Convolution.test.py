# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

#==================================================
from Convolution.AND_Convolution import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    write(" ".join(map(str,Convolution_AND(A,B))))

#==================================================
verify()
