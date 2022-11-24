# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod

#==================================================
from Sequence.Montmort_Number import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    N,M=map(int,input().split())
    write(" ".join(map(str, Montmort_Number(N,M))))

#==================================================
verify()
