with open('d6_in.txt', 'r') as f:
    G = f.readlines()
    R, C = len(G), len(G[0])

    for r in range(R):
        try:
            rs, cs = r, G[r].index('^')
        except:
            continue

SEEN = set()
pr, pc = rs, cs
d = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
while True:
    SEEN.add((pr, pc))
    nr, nc = pr + dr[d], pc + dc[d]

    if nr > R-1 or nr < 0 or nc > C-1 or nc < 0: break

    if G[nr][nc] == '#':
        d = (d+1)%4
    else:
        pr, pc = nr, nc

print(len(SEEN))

loops = 0
STATES = set()
for rr, cc in SEEN:
    STATES.clear()
    pr, pc, d = rs, cs, 0
    
    if (rr, cc) == (rs, cs): continue

    G[rr] = G[rr][:cc] + '#' + G[rr][cc+1:]

    while True:
        s = pr, pc, d
        if s in STATES:
            loops+=1
            break

        STATES.add(s)
        nr, nc = pr + dr[d], pc + dc[d]

        if nr > R-1 or nr < 0 or nc > C-1 or nc < 0: break

        if G[nr][nc] == '#':
            d = (d+1)%4
        else:
            pr, pc = nr, nc
    
    G[rr] = G[rr][:cc] + '.' + G[rr][cc+1:]

    
print(loops)

# This is a bad implementation for part 2. It takes a few seconds to run.
# I can think of several better ways to do this, but I don't want to spend the time
