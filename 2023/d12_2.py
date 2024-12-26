with open('d12.txt', 'r') as f:
    lines = [l.strip().split() for l in f.readlines()]
    flld = [a for (a,b) in lines]
    blks = [[int(e) for e in b.split(',')] for (a,b) in lines]

SEEN = dict()
def num_valid(C,B):
    K = (C,*B)
    if K in SEEN: return SEEN[K]
    
    N = len(C)
    M = sum(B) + len(B) - 1
    if M == -1:
        if '#' in C:
            SEEN[K] = 0
            return 0
        SEEN[K] = 1
        return 1

    # NOT ENOUGH SPACE
    if N < M: 
        SEEN[K] = 0
        return 0
    
    # JUST ENOUGH SPACE
    if N == M:
        opt = (''.join(['#'*b + '.' for b in B]))[:-1]
        diff = [C[i] for i in range(N) if not (C[i] == opt[i] or C[i] == '?')]
        if len(diff) == 0:
            SEEN[K] = 1
            return 1
        else:
            SEEN[K] = 0
            return 0
    
    # SPACE TO SPARE
    S = 0
    BLK = B[0]

    for p in range(0,N-M+1):
        if '.' in C[p:p+BLK] or '#' in C[:p]: continue
        if p+BLK < N and C[p+BLK] == '#': continue
        S += num_valid(C[p+BLK+1:],[*B[1:]])
    
    SEEN[K] = S
    return S

s1 = 0
s2 = 0
for C, B in zip(flld,blks):
    s1+=num_valid(C,B)
    s2+=num_valid(C+'?'+C+'?'+C+'?'+C+'?'+C,B*5)

print(s1)
print(s2)
