# Idea: compute the grid after each cycle and save the result to a dict
# along with its cycle. Once you see repetition, you can skip to the end
M = 1000000000

import numpy as np

O = []
P = set()
with open('d14_in.txt', 'r') as f:
    lines = f.read().splitlines()
    R, C = len(lines), len(lines[0])
    for r, l in enumerate(lines):
        for c, ch in enumerate(l):
            if ch == '#': 
                P.add((r,c))
            elif ch == 'O':
                O.append((r,c))
N = len(O)

fxd = set()
def cycle(O):
    # NORTH
    fxd.clear()
    O.sort(key = lambda x: x[0])
    for i in range(N):
        r,c = O[i]
        while True:
            if r == 0: break
            if (r-1,c) in P or (r-1,c) in fxd: break
            r-=1
        fxd.add((r,c))
        O[i] = (r,c)

    # WEST
    fxd.clear()
    O.sort(key = lambda x: x[1])
    for i in range(N):
        r,c = O[i]
        while True:
            if c == 0: break
            if (r,c-1) in P or (r,c-1) in fxd: break
            c-=1
        fxd.add((r,c))
        O[i] = (r,c)

    # SOUTH
    fxd.clear()
    O.sort(key = lambda x: -x[0])
    for i in range(N):
        r,c = O[i]
        while True:
            if r == R-1: break
            if (r+1,c) in P or (r+1,c) in fxd: break
            r+=1
        fxd.add((r,c))
        O[i] = (r,c)
    
    # EAST
    fxd.clear()
    O.sort(key = lambda x: -x[1])
    for i in range(N):
        r,c = O[i]
        while True:
            if c == C-1: break
            if (r,c+1) in P or (r,c+1) in fxd: break
            c+=1
        fxd.add((r,c))
        O[i] = (r,c)

# Perform cycles until repetition
Cy = 0
SEEN = dict()
while Cy < M:
    K = frozenset(O)
    if K in SEEN:
        STEP = Cy - SEEN[K]
        Cy+=((M-Cy)//STEP)*STEP
        if Cy == M: break
    SEEN[K] = Cy
    Cy+=1
    cycle(O)

print(sum([R-r for (r,c) in O]))
