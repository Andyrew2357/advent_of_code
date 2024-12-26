import heapq as hq

# part 1
BND = 70
T = 1024
with open('d18_in.txt', 'r') as f:
    C = set()
    for _ in range(T): C.add(tuple([int(s) for s in f.readline().split(',')]))

D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
Q = [(0, 0, 0, {(0,0)})]
S = {}
P = {}

while Q:
    s, x, y, p = hq.heappop(Q)
    if (x, y) in S: continue
    S[(x, y)] = s
    P[(x,y)] = p

    if (x, y) == (BND, BND):
        print(s)
        break

    for dx, dy in D:
        nx, ny = x+dx, y+dy
        if (nx, ny) in C: continue
        if nx < 0 or nx > BND: continue
        if ny < 0 or ny > BND: continue 
        hq.heappush(Q, (s+1, nx, ny, p|{(nx, ny)}))

path = P[(BND, BND)]

# part 2
with open('d18_in.txt', 'r') as f:
    C = []
    for l in f.read().splitlines(): C.append(tuple([int(s) for s in l.split(',')]))

t = T
while True:
    t+=1
    if C[t - 1] in path:
        Q = [(0, 0, 0, {(0,0)})]
        S = {}
        P = {}
        free = False
        while Q:
            s, x, y, p = hq.heappop(Q)
            if (x, y) in S: continue
            S[(x, y)] = s
            P[(x,y)] = p

            if (x, y) == (BND, BND):
                free = True
                break

            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if (nx, ny) in C[:t]: continue
                if nx < 0 or nx > BND: continue
                if ny < 0 or ny > BND: continue 
                hq.heappush(Q, (s+1, nx, ny, p|{(nx, ny)}))
        
        if not free:
            a, b = C[t-1]
            print(f'{a},{b}')
            quit()

        path = P[(BND, BND)]