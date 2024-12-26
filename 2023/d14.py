# part 1 is totally different from part 2
import numpy as np

with open('d14_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])
    R, C = grd.shape

s = 0
for c in range(C):
    P, = np.where(grd[:,c] == '#')
    P = np.insert(P,P.size,R)
    P = np.insert(P,0,-1)

    for i in range(P.size-1):
        L = np.count_nonzero(grd[P[i]+1:P[i+1],c] == 'O')
        s+=(L*(R-P[i]) - L*(L+1)//2)

print(s)
