from collections import defaultdict,deque
import itertools
import heapq
import re

L = []
BLK = []
with open('d22_in.txt', 'r') as f:
    for l in f.read().splitlines():
        x0, y0, z0, x1, y1, z1 = [int(e) for e in re.findall(r'\d+', l)]
        assert x0 <= x1 and y0 <= y1 and z0 <= z1

        heapq.heappush(BLK, (z0, x0, y0, z1, x1, y1))
        L.append((z0, x0, y0, z1, x1, y1))

A = defaultdict(list) # A[k] = bricks supported by k
B = defaultdict(list) # B[k] = bricks that support k
Z = defaultdict(lambda: (0, None)) # map of surface

while BLK:
    blk = heapq.heappop(BLK)
    z0, x0, y0, z1, x1, y1 = blk

    S = [(Z[(x, y)][0], x, y, Z[(x, y)][1]) for x, y in 
    itertools.product(range(x0, x1 +1), range(y0, y1 + 1))]
    S.sort(reverse = True)

    zm = S[0][0]
    for z_, x, y, blk_ in S:
        if not z_ == zm: break
        if blk_ is None: break

        if not blk in A[blk_]: A[blk_].append(blk)
        if not blk_ in B[blk]: B[blk].append(blk_)
    
    for x, y in itertools.product(range(x0, x1 +1), range(y0, y1 + 1)):
        Z[(x, y)] = (zm + z1 - z0 + 1, blk)

# part 2
def nfall(blk):
    Q = deque([blk])
    fallen = set()

    while Q:
        b = Q.popleft()

        if b in fallen: continue
        fallen.add(b)

        for ab in A[b]:
            F = True
            for b_ in B[ab]:
                if not b_ in fallen:
                    F = False
                    break
            
            if F: Q.append(ab)

    return len(fallen) - 1

W = 0
W_ = 0
for blk in L:
    if len(A[blk]) == 0 or min([len(B[blk_]) for blk_ in A[blk]]) > 1: 
        W+=1
    else:
        W_+=nfall(blk)

print(W)
print(W_)
