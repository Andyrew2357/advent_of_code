import heapq
import numpy as np
from collections import defaultdict, deque

with open('d16_in.txt', 'r') as f:
    B = np.array([list(s.strip()) for s in f.readlines()], dtype=str)
R, C = B.shape

r, c = np.where(B=='S')
r, c = r[0], c[0]
d = 0
D = [(0, 1), (-1, 0), (0, -1), (1, 0)]

Q = [(0, r, c, d, None),]
S = {}
P = defaultdict(set)
unfound = True
while Q:
    s, r, c, d, prev = heapq.heappop(Q)

    q = (r, c, d)
    if q in S: 
        if s == S[q]: P[(r, c, d)].add(prev)
        continue
    S[q] = s
    P[(r, c, d)].add(prev)

    if unfound and B[r, c] == 'E':
        best = s
        print(s)
        unfound = False
    
    dr, dc = D[d]
    nr, nc = r+dr, c+dc
    if not B[nr, nc] == '#': heapq.heappush(Q, (s+1, nr, nc, d, (r, c, d)))
    heapq.heappush(Q, (s+1000, r, c, (d+1)%4, (r, c, d)))
    heapq.heappush(Q, (s+1000, r, c, (d-1)%4, (r, c, d)))

er, ec = np.where(B == 'E')
er, ec = er[0], ec[0]
Q = deque()
for d in range(4):
    q = (er, ec, d)
    if S[q] == best: Q.append(q)

SEEN = set()
seats = set()
while Q:
    q = Q.popleft()
    if q in SEEN: continue
    if q is None: continue
    SEEN.add(q)
    r, c, d = q
    seats.add((r, c))

    for p in P[q]: Q.append(p)

print(len(seats))
