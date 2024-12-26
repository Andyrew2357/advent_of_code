import numpy as np
from collections import defaultdict
from math import gcd

with open('d8_in.txt', 'r') as f:
    Ch = np.array([list(s.strip()) for s in f.readlines()], dtype=str)

N, M = Ch.shape

S = defaultdict(list)
for r in range(N):
    for c in range(M):
        if not Ch[r, c] == '.': S[Ch[r, c]].append((r, c))

A = set()
def add_a(r, c):
    if not int(r) == r or not int(c) == c: return
    if r < 0 or r >= N: return
    if c < 0 or c >= M: return

    A.add((r,c))

B = set()
for k in S:
    SS = S[k]
    P = len(SS)
    for i in range(P-1):
        for j in range(i+1, P):
            r1, c1 = SS[i]
            r2, c2 = SS[j]
            add_a((2*r1+r2)/3, (2*c1+c2)/3)
            add_a((r1+2*r2)/3, (c1+2*c2)/3)
            add_a((2*r2-r1), (2*c2-c1))
            add_a((2*r1-r2), (2*c1-c2))

            Dr, Dc = r2-r1, c2-c1
            dd = gcd(Dr, Dc)
            dr, dc = Dr//dd, Dc//dd
            r, c = r1, c1
            while True:
                if r < 0 or r >= N: break
                if c < 0 or c >= M: break

                B.add((r, c))
                r, c = r+dr, c+dc

            r, c = r1, c1
            while True:
                if r < 0 or r >= N: break
                if c < 0 or c >= M: break

                B.add((r, c))
                r, c = r-dr, c-dc

print(len(A))
print(len(B))