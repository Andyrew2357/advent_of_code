import re
from collections import deque

S = 0
K = ['x', 'm', 'a', 's']
with open('d19_in.txt', 'r') as f:
    parserules = True
    R = dict()
    for l in f:
        if l == '\n':
            parserules = False
            continue

        if parserules:
            i = l.find('{')
            R[l[:i]] =l[i+1:-2].split(',')
            continue
        
        rl = 'in'
        I = {K[j]:int(s[1:]) for j, s in enumerate(re.findall(r'\=\d*', l))}
        while not rl in ['R','A']:

            for C in R[rl]:
                i = C.find(':')
                if i < 0: 
                    rl = C
                    continue
                k, cmp, n, nrl = C[0], C[1], int(C[2:i]), C[i+1:]

                if (cmp == '>' and I[k] > n) or (cmp == '<' and I[k] < n):
                    rl = nrl
                    break
        
        if rl == 'A': S+=(I['x']+I['m']+I['a']+I['s'])

print(S)

# part 2 (Interval arithmetic)
il, ih = 0, 4001

Co = {'x':0, 'm':1, 'a':2, 's':3}
Is = deque([[(il,ih),(il,ih),(il,ih),(il,ih),'in']])
As = []
while Is:
    q = Is.popleft()
    rl = q[-1]
    if rl == 'R': continue
    if rl == 'A':
        As.append(q[:-1])
        continue

    for C in R[rl]:
        i = C.find(':')
        if i < 0:
            qn = q.copy()
            qn[-1] = C
            Is.append(qn)
            continue
        
        k, cmp, n, nrl = Co[C[0]], C[1], int(C[2:i]), C[i+1:]

        match cmp:
            case '>':
                if n > q[k][1]: continue
                qh = q.copy()
                qh[k] = (max(q[k][0], n), q[k][1])
                qh[-1] = nrl
                Is.append(qh)
                
                if n <= q[k][0]: break
                q[k] = (q[k][0], min(q[k][1], n)+1)
            
            case '<':
                if n < q[k][0]: continue
                ql = q.copy()
                ql[k] = (q[k][0], min(q[k][1], n))
                ql[-1] = nrl
                Is.append(ql)

                if n >= q[k][1]: break
                q[k] = (max(q[k][0], n)-1, q[k][1])

def vol(hcube):
    p = 1
    for s in hcube: p*=(s[1]-s[0]-1)
    return p

print(sum([vol(h) for h in As]))
