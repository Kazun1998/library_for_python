# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lcm_convolution

#==================================================
from Convolution.LCM_Convolution import Convolution_LCM

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=[0]+list(map(int,input().split()))
    B=[0]+list(map(int,input().split()))
    write(" ".join(map(str,Convolution_LCM(A,B,N)[1:])))

#==================================================
verify()