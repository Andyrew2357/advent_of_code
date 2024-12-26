# working solution

import numpy as np
from collections import deque

with open('d16_ex.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R, C = grd.shape

def beamlen(r,c,d):
    SEEN = set()
    E = set()
    Q = deque([(r,c,d)])

    def appendQ(r,c,d):
        if r < 0 or r >= R: return
        if c < 0 or c >= C: return
        Q.append((r,c,d))

    D = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}
    while Q:
        q = Q.popleft()
        if q in SEEN: continue
        
        r, c, d = q
        dr, dc = D[d]
        SEEN.add(q)
        E.add((r,c))

        if grd[r,c] == '.':
            appendQ(r+dr,c+dc,d)
            continue

        if grd[r,c] == '|':
            if d in 'LR':
                appendQ(r-1,c,'U')
                appendQ(r+1,c,'D')
            else:
                appendQ(r+dr,c+dc,d)
            continue

        if grd[r,c] == '-':
            if d in 'UD':
                appendQ(r,c-1,'L')
                appendQ(r,c+1,'R')
            else:
                appendQ(r+dr,c+dc,d)
            continue
        
        if grd[r,c] == '/':
            match d:
                case 'R': appendQ(r-1,c,'U')
                case 'L': appendQ(r+1,c,'D')
                case 'U': appendQ(r,c+1,'R')
                case 'D': appendQ(r,c-1,'L')
            continue

        if grd[r,c] == '\\':
            match d:
                case 'R': appendQ(r+1,c,'D')
                case 'L': appendQ(r-1,c,'U')
                case 'U': appendQ(r,c-1,'L')
                case 'D': appendQ(r,c+1,'R')
            continue
    
    return len(E)

print(beamlen(0,0,'R'))

RL = [beamlen(r,0,'R') for r in range(R)]
LL = [beamlen(r,C-1,'L') for r in range(R)]
UL = [beamlen(R-1,c,'U') for c in range(C)]
DL = [beamlen(0,c,'D') for c in range(C)]

print(max([max(RL),max(LL),max(UL),max(DL)]))

print(RL)
