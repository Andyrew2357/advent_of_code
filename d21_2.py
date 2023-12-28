# Part 2: Notice that the puzzle input has an important feature
# along the middle row and column, namely that there are no rocks
# These are the N,E,S,W highways, and they are particularly useful
# since our metric is manhatten distance.

# There are also highways all around the edge of the grid, which
# might be useful as well.

# R = C = 131, which is odd. This means that the checkerboard
# pattern on adjacent grids has opposite parity.

# n = M//R = 202300. 2*n*(n+1) = 81850984600. This is the number
# of reachable grid centers, though only the ones on the boundary
# will matter. The interior calculation can largely be skipped.
# There are still 4*n grids just on the immediate boundary, so 
# more optimizations are needed. Actually, I think that each of
# the boundary grids can largely be treated the same dependent on
# what side of the diamond they're on. 

# Because of the highways, the distance from the origin of any 
# boundary point on an outlying grid is actually just its manhatten 
# distance, because we are allowed to take rectilinear paths. This
# means we can treat all grids in the ith diamond ring around the 
#center indistinguishably and compute the minimum distance from a 
# boundary point to calculate the distance of any interior point
# from the origin. This can be precomputed with the initial grid.
# Once these are computed, the remaining computation becomes easy.

# precompute the distances of interior coordinates from boundaries
# when approaching from different directions (N,NE,E,SE,S,SW,W,NW)

from collections import defaultdict
import itertools
import numpy as np
import heapq

with open('d21_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R,C = grd.shape
r0, c0 = R//2, C//2

def precomputeDst(Q):
    DST = defaultdict(lambda: 1e9)
    while Q:
        q = heapq.heappop(Q)
        d, r, c = q

        if (r, c) in DST: continue
        DST[(r, c)] = d

        for dr,dc in [(-1, 0), (0, -1), (0, 1), (1,0)]:
            if not 0 <= r + dr < R: continue
            if not 0 <= c + dc < C: continue
            if grd[r + dr, c + dc] == '#': continue
            heapq.heappush(Q, (d + 1, r + dr, c + dc))
    
    return DST

Dst = dict()

Dst['N'] = precomputeDst([(0,R-1,c0)])
Dst['S'] = precomputeDst([(0,0,c0)])
Dst['W'] = precomputeDst([(0,r0,C-1)])
Dst['E'] = precomputeDst([(0,r0,0)])

Dst['NE'] = precomputeDst([(0,R-1,0)])
Dst['SE'] = precomputeDst([(0,0,0)])
Dst['SW'] = precomputeDst([(0,0,C-1)])
Dst['NW'] = precomputeDst([(0,R-1,C-1)])

# Compute hits on an interior rings with given parity
# First compute reachable tiles
OP = [(r, c) for r, c in itertools.product(range(R), range(C)) if Dst['N'][(r, c)] < 1e9]

M = 26501365
# M = 1180148 this was for the example

ev, od = M%2, (M + 1)%2
EV = len([1 for r, c in OP if (r + c)%2 == ev])
OD = len([1 for r, c in OP if (r + c)%2 == od])

# compute how far the interior extends
N = (M - r0)//R - 2

# compute the hits for all interior grids
NEV = 4*(N//2)*(N//2 + 1) + 1
NOD = 4*((N + 1)//2)**2
W = NEV*EV + NOD*OD

# compute hits on the outlying rings
def ringhits(I):
    S = 0
    hp = ev if (I)%2 == 0 else od

    # there is one grid each for N, S, W, & E
    # there are N each for NW, NE, SW, SE

    S+=len([1 for r, c in OP if (r + c)%2 == hp and Dst['N'][(r, c)] + (I-1)*R + r0 + 1 <= M])
    S+=len([1 for r, c in OP if (r + c)%2 == hp and Dst['S'][(r, c)] + (I-1)*R + r0 + 1 <= M])
    S+=len([1 for r, c in OP if (r + c)%2 == hp and Dst['W'][(r, c)] + (I-1)*R + r0 + 1 <= M])
    S+=len([1 for r, c in OP if (r + c)%2 == hp and Dst['E'][(r, c)] + (I-1)*R + r0 + 1 <= M])

    S+=(I - 1)*len([1 for r, c in OP if (r + c)%2 == hp and Dst['NW'][(r, c)] + (I-1)*R + 1 <= M])
    S+=(I - 1)*len([1 for r, c in OP if (r + c)%2 == hp and Dst['NE'][(r, c)] + (I-1)*R + 1 <= M])
    S+=(I - 1)*len([1 for r, c in OP if (r + c)%2 == hp and Dst['SW'][(r, c)] + (I-1)*R + 1 <= M])
    S+=(I - 1)*len([1 for r, c in OP if (r + c)%2 == hp and Dst['SE'][(r, c)] + (I-1)*R + 1 <= M])

    return S

for i in range(N + 1, N + 4): 
    if ringhits(i) == 0: print('wow')
    W+=ringhits(i)

print(W)

# after looking at some people's solutions on the subreddit,
# I think a few of them might just get lucky with an input that
# admits a tiling solution, but I could be mistaken.