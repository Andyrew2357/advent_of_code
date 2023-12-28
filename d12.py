with open('d12.txt', 'r') as f:
    lines = [l.strip().split() for l in f.readlines()]
    flld = [a for (a,b) in lines]
    blks = [[int(e) for e in b.split(',')] for (a,b) in lines]

pkeys = dict()
def part(n,k):
    if n == 1: return [[k]]
    if (n,k) in pkeys: return pkeys[(n,k)]
    P = []
    for i in range(0,k+1):
        for subp in part(n-1,k-i):
            P.append([i,*subp])   
    pkeys[(n,k)] = P
    return P

def num_valid(C,B):
    b = ['#'*e + '.' for e in B]
    b[-1]=b[-1][:-1]
    m = len(B) + 1
    n = len(C) - (sum(B) + m - 2)

    S = 0
    for P in part(m,n):
        opt = ''.join(['.'*P[i] + b[i] for i in range(m-1)])
        opt+=('.'*P[-1])
        diff = [C[i] for i in range(len(C)) if not opt[i] == C[i]]
        if '.' in diff or '#' in diff: continue
        S+=1
    
    return S

s1 = 0
for C, B in zip(flld,blks):
    s1+=num_valid(C,B)

print(s1)
