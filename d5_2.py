from collections import defaultdict

with open('d5_in.txt', 'r') as f:
    lines=f.readlines()

seeds = [int(c) for c in lines[0].strip().split()[1:]]
intvls = [(seeds[e], seeds[e] + seeds[e + 1] - 1) for e in range(0,len(seeds),2)]

parts = defaultdict(list)
maps = dict()
func = dict()

mapid = 0
for l in lines[2:]:
    if 'to' in l: continue

    if l == '\n':
        maps[mapid] = func.copy()
        func.clear()
        mapid+=1
        continue
    
    a, b, c = [int(e) for e in l.strip().split()]
    func[(b,b+c-1)]=a-b

    cuts=[b,b+c]
    for o in cuts: 
        if not o in parts[mapid]: parts[mapid].append(o) 


def eval_num(s,n):
    cur = s
    for key in maps[n]:
        a, b = key
        if a <= cur and cur <= b:
            cur+=maps[n][key]
            break
    return cur

def eval_intvl(intvl,n):
    new_intvl=[]

    par = parts[n]
    for I in intvl:
        a,b=I
        cuts = [p for p in par if a < p and p < b]
        cuts.append(a)
        cuts.sort()
        N = len(cuts)
        for i in range(0,N-1):
            new_intvl.append((eval_num(cuts[i],n),eval_num(cuts[i+1] - 1,n)))
        new_intvl.append((eval_num(cuts[-1],n),eval_num(b,n)))

    return new_intvl

for j in range(mapid):
    intvls = eval_intvl(intvls,j)

lbounds = [a for a,b in intvls]

print(min(lbounds))
