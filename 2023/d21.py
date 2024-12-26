M = 64

import numpy as np
import heapq

with open('d21_ex.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R,C = grd.shape
r0, c0 = R//2, C//2

Q = [(0, r0, c0)]
D = set()
W = 0
while Q:
    q = heapq.heappop(Q)
    d, r, c = q

    if d > M: break
    if (r, c) in D: continue
    if (r + c - r0 - c0)%2 == 0: W+=1
    D.add((r, c))

    for dr,dc in [(-1, 0), (0, -1), (0, 1), (1,0)]:
        if not 0 <= r + dr < R: continue
        if not 0 <= c + dc < C: continue
        if grd[r + dr, c + dc] == '#': continue
        heapq.heappush(Q, (d + 1, r + dr, c + dc))

print(W)
