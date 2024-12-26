from collections import deque, defaultdict
import heapq
import numpy as np

with open('d23_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R,C = grd.shape

# First simplify the grid by replacing redundant nodes
# with single paths.
    
PATH = defaultdict(list)
    
Q = deque([(1, 1, 1, (0, 1))])
EXP = {(0, 1)}

while Q:
    d, r, c, PN = Q.popleft()

    if (r, c) == (R - 1, C - 2): 
        PATH[PN].append(((r, c), d))
        PATH[(r, c)].append((PN, d))
        continue

    OPT = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if grd[r + dr, c + dc] == '#': continue
        if (r + dr, c + dc) in EXP: continue
        OPT.append((r + dr, c + dc))

    EXP.add((r, c))
    if len(OPT) == 0: 
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if not (r + dr, c + dc) in PATH: continue
            if PN == (r + dr, c + dc): continue
            PATH[(r + dr, c + dc)].append((PN, d + 1))
            PATH[PN].append(((r + dr, c + dc), d + 1))     
        continue
    
    if len(OPT) == 1: 
        Q.appendleft((d + 1, *OPT[0], PN))
        continue

    for q in OPT: 
        Q.append((1, *q, (r, c)))

    if (r, c) in PATH[PN]: continue
    PATH[PN].append(((r, c), d))
    PATH[(r, c)].append((PN, d))

M = 0
SEEN = defaultdict(lambda: False)
def DFS(N, D):
    global M
    if SEEN[N]: return
    SEEN[N] = True
    
    if N == (R - 1, C - 2): M = max(M, D)

    for NN, DD in PATH[N]:
        DFS(NN, D + DD)
    
    SEEN[N] = False

DFS((0, 1), 0)
print(M)
