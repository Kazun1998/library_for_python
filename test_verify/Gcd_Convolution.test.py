# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_convolution

#==================================================
import sys
from Convolution.GCD_Convolution import Convolution_GCD

input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())
    A=[0]+list(map(int,input().split()))
    B=[0]+list(map(int,input().split()))

    write(" ".join(map(str,Convolution_GCD(A,B)[1:])))

#==================================================
verify()
