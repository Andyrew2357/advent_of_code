with open('d9_in.txt', 'r') as f:
    L = f.read().strip()

N = len(L)
m = (N+1)//2
B = {i:int(L[2*i]) for i in range(m)}
NN = sum([B[i] for i in B])

s = 0
mm = m-1
ind = 0
for i in range(N):
    if ind >= NN: break

    n = int(L[i])
    if i%2 == 0:
        nn = min(n, NN-ind)
        s+=(nn*ind+nn*(nn-1)//2)*(i//2)
        ind+=nn
    else:
        for j in range(n):
            while B[mm] == 0: mm-=1
            s+=mm*ind
            B[mm]-=1
            ind+=1

print(s)

# part 2
import numpy as np
Sp = np.array([int(l) for l in L], dtype=int)
St = np.cumsum(Sp, dtype=int)-Sp

# space id: space available, starting index of remaining
SPA = {i:(0, St[i]) if i%2 == 0 else (Sp[i], St[i]) for i in range(N)}

BLO = {i:int(L[2*i]) for i in range(m)}
s=0
for b in sorted(BLO.keys(), reverse=True):
    blob = BLO[b]
    f = False
    for spid in SPA:
        if spid >= b*2: break
        sp, st = SPA[spid]
        if sp >= blob:
            f=True
            SPA[spid] = (sp-blob, st+blob)
            s+=b*(blob*int(st)+blob*(blob-1)//2)
            break
    if not f:
        s+=b*(blob*int(St[2*b])+blob*(blob-1)//2)

print(s)