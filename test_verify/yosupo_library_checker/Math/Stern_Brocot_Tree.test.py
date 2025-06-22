# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stern_brocot_tree

#==================================================
from Stern_Brocot_Tree import *

import sys
input=sys.stdin.readline
write=sys.stdout.write

#==================================================
def verify():
    T = int(input())

    ans = [None] * T
    for t in range(T):
        command, *value = input().split()
        if command == 'ENCODE_PATH':
            a, b = map(int, value)
            code = Stern_Brocot_Tree.encode(a, b)
            ans[t] = ' '.join([str(len(code))] + [f'{c} {n}' for c, n in code])
        elif command == 'DECODE_PATH':
            k, *seq = value
            k = int(k)
            code = [(seq[2 * i], int(seq[2 * i + 1])) for i in range(k)]
            a, b = Stern_Brocot_Tree.decode(code)
            ans[t] = f'{a} {b}'
        elif command == 'LCA':
            a, b, c, d = map(int, value)
            f, g = Stern_Brocot_Tree.lowest_common_ancestor(a, b, c, d)
            ans[t] = f'{f} {g}'
        elif command == 'ANCESTOR':
            k, a, b = map(int, value)
            f, g = Stern_Brocot_Tree.ancestor(a, b, k, (None, None))
            if f is None:
                ans[t] = '-1'
            else:
                ans[t] = f'{f} {g}'
        elif command == 'RANGE':
            a, b = map(int, value)
            f, g, h, k = Stern_Brocot_Tree.range(a, b)
            ans[t] = f'{f} {g} {h} {k}'
    return ans

#==================================================

write("\n".join(map(str, verify())))
