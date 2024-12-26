with open('d15_in.txt', 'r') as f:
    B = []
    r=0
    while True:
        l = f.readline().strip()
        if l == '': break
        try:
            rc = l.index('@')
            rr = r
            l = l[:rc] + '.' + l[rc+1:]
        except:
            pass
        B.append(list(l))
        r+=1

    M = []
    for l in f.read().splitlines(): M.extend(list(l))
    R, C = len(B), len(B[0])

# debug tool
def disp():
    for r in range(R):
        if r == rr:
            l = B[r].copy()
            l[rc] = '@'
            print(''.join(l))
        else:
            print(''.join(B[r]))


D = {'>':(0, 1), '^':(-1, 0), '<':(0, -1), 'v':(1, 0)}
def move(r, c, d):
    dr, dc = D[d]
    nr, nc = r+dr, c+dc
    match B[nr][nc]:
        case '.': 
            B[nr][nc] = B[r][c]
            B[r][c] = '.'
        case 'O': 
            move(nr, nc, d)
            if B[nr][nc] == '.':
                B[nr][nc] = B[r][c]
                B[r][c] = '.'
        case '#':
            return

for m in M: 
    dr, dc = D[m]
    nr, nc = rr+dr, rc+dc
    if B[nr][nc] == 'O': move(nr, nc, m)
    if B[nr][nc] == '.': rr, rc = nr, nc

s1 = 0
for r in range(R):
    for c in range(C):
        if B[r][c] == 'O': s1+=100*r+c

if False: disp()
print(s1)

# part 2

with open('d15_in.txt', 'r') as f:
    B = []
    r=0
    while True:
        l = f.readline().strip()
        l = l.replace('#', '##')
        l = l.replace('.', '..')
        l = l.replace('O', '[]')
        l = l.replace('@', '@.')
        if l == '': break
        try:
            rc = l.index('@')
            rr = r
            l = l[:rc] + '.' + l[rc+1:]
        except:
            pass
        B.append(list(l))
        r+=1

    M = []
    for l in f.read().splitlines(): M.extend(list(l))
    R, C = len(B), len(B[0])

def avail(r, c, d):
    dr, dc = D[d]
    nr, nc = r+dr, c+dc

    match B[nr][nc]:
        case '.': return True
        case '#': return False
        case '[': 
            if d in ['^', 'v']: return avail(nr, nc, d) and avail(nr, nc+1, d)
            if d == '>': return avail(nr, nc+1, d)
        case ']':
            if d in ['^', 'v']: return avail(nr, nc, d) and avail(nr, nc-1, d)
            if d == '<': return avail(nr, nc-1, d)

def make_move(r, c, d):
    dr, dc = D[d]
    nr, nc = r+dr, c+dc
    match B[r][c]:
        case '.': return
        case '[':
            if d in ['^', 'v']:
                make_move(nr, nc, d)
                if not B[nr][nc] == '[': make_move(nr, nc+1, d)
                B[r][c] = '.'
                B[r][c+1] = '.'
                B[nr][nc] = '['
                B[nr][nc+1] = ']'
            else:
                make_move(nr, nc, d)
                B[r][c] = '.'
                B[nr][nc] = '['
        case ']':
            if d in ['^', 'v']:
                make_move(nr, nc, d)
                if not B[nr][nc] == ']': make_move(nr, nc-1, d)
                B[r][c] = '.'
                B[r][c-1] = '.'
                B[nr][nc] = ']'
                B[nr][nc-1] = '['
            else:
                make_move(nr, nc, d)
                B[r][c] = '.'
                B[nr][nc] = ']'

for m in M:
    dr, dc = D[m]
    nr, nc = rr+dr, rc+dc
    if avail(rr, rc, m):
        rr, rc = nr, nc
        make_move(rr, rc, m)

s2 = 0
for r in range(R):
    for c in range(C):
        if B[r][c] == '[': s2+=100*r+c

if False: disp()
print(s2)