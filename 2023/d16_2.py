# THIS CURRENTLY DOES NOT WORK

# For some reason I don't totally understand, this isn't reliable.
# I might try to fix it at some point, though the whole point was
# just to try and do it more efficiently than my original solution.

import numpy as np
import sys
sys.setrecursionlimit(10000)

with open('d16_ex.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R, C = grd.shape

SEEN = dict()
D = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}
def beam(r,c,d,par=set()):
    if r < 0 or r >= R: return set()
    if c < 0 or c >= C: return set()
    
    K = (r,c,d)
    if K in SEEN: return SEEN[K]
    if K in par: return set()
    P = {K}.union(par.copy())

    dr, dc = D[d]
    if grd[r,c] == '.':
        res = {(r,c)}.union(beam(r+dr,c+dc,d,P))

    if grd[r,c] == '|':
        if d in 'LR':
            res = {(r,c)}.union(beam(r-1,c,'U',P),beam(r+1,c,'D',P))
        else:
            res = {(r,c)}.union(beam(r+dr,c+dc,d,P))

    if grd[r,c] == '-':
        if d in 'UD':
            res = {(r,c)}.union(beam(r,c-1,'L',P),beam(r,c+1,'R',P))
        else:
            res = {(r,c)}.union(beam(r+dr,c+dc,d,P))
    
    if grd[r,c] == '/':
        match d:
            case 'R': res = {(r,c)}.union(beam(r-1,c,'U',P))
            case 'L': res = {(r,c)}.union(beam(r+1,c,'D',P))
            case 'U': res = {(r,c)}.union(beam(r,c+1,'R',P))
            case 'D': res = {(r,c)}.union(beam(r,c-1,'L',P))

    if grd[r,c] == '\\':
        match d:
            case 'R': res = {(r,c)}.union(beam(r+1,c,'D',P))
            case 'L': res = {(r,c)}.union(beam(r-1,c,'U',P))
            case 'U': res = {(r,c)}.union(beam(r,c-1,'L',P))
            case 'D': res = {(r,c)}.union(beam(r,c+1,'R',P))
    
    SEEN[K] = res.copy()
    return res

def beamlen(r,c,d): return len(beam(r,c,d))

print(beamlen(0,0,'R'))

RL = [beamlen(r,0,'R') for r in range(R)]
LL = [beamlen(r,C-1,'L') for r in range(R)]
UL = [beamlen(R-1,c,'U') for c in range(C)]
DL = [beamlen(0,c,'D') for c in range(C)]

print(max([max(RL),max(LL),max(UL),max(DL)]))

print(RL)
