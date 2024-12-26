BND = 100
with open('d20_in.txt', 'r') as f:
    B = [list(l) for l in f.read().splitlines()]
    for i in range(len(B)):
        if 'S' in B[i]: 
            rr, cc = i, B[i].index('S')
            break

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
P = {}
d = 0
r, c = rr, cc 
while True:
    P[(r, c)] = d
    if B[r][c] == 'E': break
    for dr, dc in D:
        nr, nc = r+dr, c+dc
        if (nr, nc) in P: continue
        if B[nr][nc] == '#': continue
        r, c = nr, nc
        break
    d+=1

s1 = 0
for r, c in P:
    for dr, dc in D:
        nr, nc = r+2*dr, c+2*dc
        if not (nr, nc) in P: continue
        if P[(nr, nc)] - P[(r, c)] > BND + 1: s1+=1

print(s1)

s2 = 0
for r, c in P:
    for dr in range(-20, 21):
        for dc in range(-20, 21):
            d = abs(dr) + abs(dc)
            if d > 20: continue
            nr, nc = r+dr, c+dc
            if not (nr, nc) in P: continue
            if P[(nr, nc)] - P[(r, c)] - d >= BND: s2+=1

print(s2)
