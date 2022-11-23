# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
# verification-helper: IGNORE

#==================================================
import sys
sys.path.append("../../../")
from Modulo_Sequence.Modulo_Polynomial import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N=int(input())

    A=list(map(int,input().split()))
    P=Modulo_Polynomial(A,N)

    try:
        write(" ".join(map(str, Sqrt(P).resize(N,True))))
    except:
        print(-1)

#==================================================
verify()
