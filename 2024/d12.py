import numpy as np

with open('d12_in.txt', 'r') as f:
    B = np.array([list(s.strip()) for s in f.readlines()], dtype=str)
R, C = B.shape

PLT = {}
SEEN = set()
Drc = [(0,1), (0, -1), (1, 0), (-1, 0)]
def add_sq(k, r, c):
    if not k in PLT: PLT[k] = {'ch':B[r,c], 'a':{(r,c)}, 'e':set(), 's':0}
    if r<0 or r>=R or c<0 or c>=R: return
    SEEN.add((r,c))
    PLT[k]['a'].add((r,c))

    for dr, dc in Drc:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=R or nc<0 or nc>=C: 
            PLT[k]['e'].add(frozenset({(r,c),(nr,nc)}))
        elif not B[nr, nc] == PLT[k]['ch']:
            PLT[k]['e'].add(frozenset({(r,c),(nr,nc)}))
        elif not (nr,nc) in PLT[k]['a']:
            add_sq(k, nr, nc)

i = 0
for r in range(R):
    for c in range(C):
        if (r,c) in SEEN: continue
        i+=1
        add_sq(i, r, c)

print(sum([len(PLT[k]['a'])*len(PLT[k]['e']) for k in PLT]))

USED = set()
def follow(k, e):
    if e in USED: return
    USED.add(e)
    p1, p2 = list(e)
    r1, c1 = p1
    r2, c2 = p2
    if r1 == r2:
        if not r1-1 < 0: 
            adj = frozenset({(r1-1,c1),(r1-1,c2)})
            if adj in PLT[k]['e']: 
                if (r1-1,c1) in PLT[k]['a'] and (r1, c1) in PLT[k]['a']: follow(k, adj)
                if (r1-1,c2) in PLT[k]['a'] and (r1, c2) in PLT[k]['a']: follow(k, adj)
        if not r1+1 >= R:
            adj = frozenset({(r1+1,c1),(r1+1,c2)})
            if adj in PLT[k]['e']:
                if (r1+1,c1) in PLT[k]['a'] and (r1, c1) in PLT[k]['a']: follow(k, adj)
                if (r1+1,c2) in PLT[k]['a'] and (r1, c2) in PLT[k]['a']: follow(k, adj)
    else:
        if not c1-1 < 0: 
            adj = frozenset({(r1,c1-1),(r2,c1-1)})
            if adj in PLT[k]['e']:
                if (r1,c1-1) in PLT[k]['a'] and (r1, c1) in PLT[k]['a']: follow(k, adj)
                if (r2,c1-1) in PLT[k]['a'] and (r2, c1) in PLT[k]['a']: follow(k, adj)
        if not c1+1 >= R:
            adj = frozenset({(r1,c1+1),(r2,c1+1)})
            if adj in PLT[k]['e']: 
                if (r1,c1+1) in PLT[k]['a'] and (r1, c1) in PLT[k]['a']: follow(k, adj)
                if (r2,c1+1) in PLT[k]['a'] and (r2, c1) in PLT[k]['a']: follow(k, adj)

for k in PLT:
    USED.clear()
    for e in PLT[k]['e']:
        if e in USED: continue
        PLT[k]['s']+=1
        follow(k, e)

print(sum([len(PLT[k]['a'])*PLT[k]['s'] for k in PLT]))
