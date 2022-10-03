# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

#==================================================
import sys
sys.path.append('Convolution/')
from AND_Convolution import *

input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    import sys
    input=sys.stdin.readline
    write=sys.stdout.write

    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    write(" ".join(map(str,Convolution_AND(A,B))))

#==================================================
verify()