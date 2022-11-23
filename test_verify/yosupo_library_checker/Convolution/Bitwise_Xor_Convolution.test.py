# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution

#==================================================
from Convolution.XOR_Convolution import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    write(" ".join(map(str,Convolution_XOR(A,B))))

#==================================================
verify()
