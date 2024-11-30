# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence

#==================================================
from Sequence.Longest_Increasing_Subsequence import *

import sys
input = sys.stdin.readline
write = sys.stdout.write

#==================================================
def verify():
    N = int(input())
    A = list(map(int, input().split()))

    res =Longest_Increasing_Subsequence(A, equal = False)

    print(res['length'])
    write(" ".join(map(str, res['index'])))

#==================================================
verify()
