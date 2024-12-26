import numpy as np
import heapq

with open('d23_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R,C = grd.shape

Q = [(0, 0, 1, set())]
M = 0

while Q:
    q = heapq.heappop(Q)
    d, r, c, P = q

    if (r, c) == (R - 1, C - 2): 
        M = max(M, -d)
        continue

    P_ = {(r, c)}.union(P)
    match grd[(r, c)]:
        case '^':
            if (r - 1, c) in P: continue
            heapq.heappush(Q, (d - 1, r - 1, c, P_))
        case 'v':
            if (r + 1, c) in P: continue
            heapq.heappush(Q, (d - 1, r + 1, c, P_))
        case '<':
            if (r, c - 1) in P: continue
            heapq.heappush(Q, (d - 1, r, c - 1, P_))
        case '>':
            if (r, c + 1) in P: continue
            heapq.heappush(Q, (d - 1, r, c + 1, P_))
        case '.':
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grd[r + dr, c + dc] == '#': continue
                if (r + dr, c + dc) in P: continue
                heapq.heappush(Q, (d - 1, r + dr, c + dc, P_))

print(M)

# This is too slow for part 2. To speed things up properly,
# we need to simplify the grid. There are large sections that
# can be replaced with single paths.
