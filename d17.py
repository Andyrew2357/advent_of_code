import numpy as np
import heapq
from collections import defaultdict

with open('d17_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[int(ch) for ch in l] for l in lines])
    R,C = grd.shape

Dst = defaultdict(lambda:1e9)
Dst[(0,0,'-')] = 0
Dst[(0,0,'|')] = 0
Q = [(0,0,0,'NA')]

def appendQ(r,c,nr,nc,d,dr):
    if nr < 0 or nr >= R: return
    if nc < 0 or nc >= R: return
    if nr == r: 
        cost = np.sum(grd[r,min(c+1,nc):max(c,nc+1)])
    else:
        cost = np.sum(grd[min(r+1,nr):max(r,nr+1),c])
    heapq.heappush(Q, (d+cost,nr,nc,dr))

while Q:
    q = heapq.heappop(Q)
    d, r, c, dr = q
    
    if (r,c,dr) in Dst: continue
    Dst[(r,c,dr)] = d

    if (r,c) == (R-1,C-1): continue

    if not dr == '|':
        for s in [1,2,3]:
            appendQ(r,c,r-s,c,d,'|')
            appendQ(r,c,r+s,c,d,'|')

    if not dr == '-':
        for s in [1,2,3]:
            appendQ(r,c,r,c-s,d,'-')
            appendQ(r,c,r,c+s,d,'-')

print(min(Dst[(R-1,C-1,'-')],Dst[(R-1,C-1,'|')]))

# part 2

Dst = defaultdict(lambda:1e9)
Dst[(0,0,'-')] = 0
Dst[(0,0,'|')] = 0
Q = [(0,0,0,'NA')]

while Q:
    q = heapq.heappop(Q)
    d, r, c, dr = q
    
    if (r,c,dr) in Dst: continue
    Dst[(r,c,dr)] = d

    if (r,c) == (R-1,C-1): continue

    if not dr == '|':
        for s in [4,5,6,7,8,9,10]:
            appendQ(r,c,r-s,c,d,'|')
            appendQ(r,c,r+s,c,d,'|')

    if not dr == '-':
        for s in [4,5,6,7,8,9,10]:
            appendQ(r,c,r,c-s,d,'-')
            appendQ(r,c,r,c+s,d,'-')

print(min(Dst[(R-1,C-1,'-')],Dst[(R-1,C-1,'|')]))