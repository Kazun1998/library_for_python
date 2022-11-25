# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm

#==================================================
from Sequence.Z_Algorithm import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    S=input()[:-1]
    write(" ".join(map(str,Z_Algorithm(S))))

#==================================================
verify()
