from collections import defaultdict

with open('d15_in.txt','r') as f:
    code = f.readline().strip().split(',')

def h(l):
    s=0
    for ch in l: s=17*(s+ord(ch))
    return s%256

print(sum([h(c) for c in code]))

box = defaultdict(list)
foc = dict()
for l in code:
    if '-' in l:
        try: 
            box[h(l[:-1])].remove(l[:-1])
        except ValueError:
            pass
        continue
    a, n = l[:-2], h(l[:-2])
    if not a in box[n]: box[n].append(a)
    foc[a] = int(l[-1])

print(sum([(e+1)*sum([(i+1)*foc[box[e][i]] for i in range(len(box[e]))]) for e in range(256)]))