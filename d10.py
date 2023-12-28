import numpy as np

with open('d10_in.txt', 'r') as f:
    lines = np.array(f.read().splitlines(), dtype=str)
    grd = np.array([[ch for ch in l] for l in lines])

r0, c0 = [e[0] for e in np.where(grd == 'S')]
pr, pc = r0, c0

Dr = [-1, 0, 0, 1]
Dc = [0, -1, 1, 0]
Con = ['|F7', '-FL', '-7J', '|LJ']
byS = set()
for dr, dc, con in zip(Dr, Dc, Con): 
    if grd[r0+dr,c0+dc] in con:
        r, c = r0+dr, c0+dc
        byS.add((dr,dc))

connect = {'|':((-1,0),(1,0)), 'F':((0,1),(1,0)), '7':((0,-1),(1,0)),
           '-':((0,-1),(0,1)), 'L':((-1,0),(0,1)), 'J':((0,-1),(-1,0))}
curve = {(r0,c0)}
while not grd[r,c] == 'S':
    curve.add((r,c))
    for dr, dc in connect[grd[r,c]]:
        if r+dr == pr and c+dc == pc: continue
        pr, pc = r, c
        r, c = r+dr, c+dc
        break

print(len(curve)//2)

# I think I can exploit an idea from the Jordan curve theorem. 
# I can go row by row and decide whether I'm inside or outside
# based on the number of crossings.

# Annoying subtlety, I have to replace S with its pipe equivalent.

for k in connect:
    if len(byS.intersection(set(connect[k]))) == 2:
        grd[r0,c0] = k
        break

enc = 0

R, C = grd.shape
for r in range(R): 
    inside = False
    for c in range(C):
        if (r,c) in curve: 
            ch = grd[r,c]
            if ch == '|': inside = not inside
            if ch == 'L': 
                ca = c+1
                while grd[r,ca] == '-': ca+=1
                if grd[r,ca] == '7': inside = not inside
            if ch == 'F':
                ca = c+1
                while grd[r,ca] == '-': ca+=1
                if grd[r,ca] == 'J': inside = not inside
            continue
        if inside: 
            enc+=1

print(enc)
# There are probably nicer ways to do this with regex