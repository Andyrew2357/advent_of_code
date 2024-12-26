import numpy as np
from collections import deque, defaultdict

with open('d10_in.txt', 'r') as f:
    B = np.array([list(s.strip()) for s in f.readlines()], dtype=int)
R, C = B.shape

Z = list(zip(*np.where(B==0)))
Q = deque([(*z, z) for z in Z])
SCORE = defaultdict(int)
SEEN = set()

Dr = [-1, 0, 1, 0]
Dc = [0, -1, 0, 1]
while Q:
    st = Q.popleft()
    if st in SEEN: continue
    SEEN.add(st)

    r, c, z = st
    if B[r, c] == 9: SCORE[z]+=1

    for dr, dc in zip(Dr, Dc):
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= R: continue
        if nc < 0 or nc >= C: continue
        if B[nr, nc] == B[r, c] + 1: Q.append((nr, nc, z))

print(sum([SCORE[z] for z in Z]))


SEEN = {}
Dr = [-1, 0, 1, 0]
Dc = [0, -1, 0, 1]
def ntrails(st):
    if st in SEEN: return SEEN[st]

    r, c = st
    if B[r, c] == 9:
        SEEN[st] = 1
        return 1

    n = 0
    for dr, dc in zip(Dr, Dc):
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= R: continue
        if nc < 0 or nc >= C: continue
        if B[nr, nc] == B[r, c] + 1: n+=ntrails((nr, nc))

    SEEN[st] = n
    return n

print(sum([ntrails(z) for z in Z]))
