
with open('d5_in.txt', 'r') as f:
    lines=f.readlines()

seeds = [int(c) for c in lines[0].strip().split()[1:]]

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

res=[]
for s in seeds:
    cur = s
    for i in range(mapid):
        for key in maps[i]:
            a, b = key
            if a <= cur and cur <=b:
                cur+=maps[i][key]
                break
    
    res.append(cur)

print(min(res))