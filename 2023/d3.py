from collections import defaultdict

with open('d3_in.txt','r') as f:
    lines=f.readlines()

rows=len(lines)
cols=len(lines[0])

Dr=[-1,-1,-1,0,0,1,1,1]
Dc=[-1,0,1,-1,1,-1,0,1]

s=0
num=0
good=False
for r in range(rows):
    for c in range(cols):
        ch = lines[r][c]
        if not ch in '1234567890':
            if good:
                # print(num) 
                s+=num
            
            good=False
            num=0
            continue
        
        if ch.isdigit():
            num = 10*num + int(ch)

            for dr,dc in zip(Dr,Dc):
                try:
                    if not lines[r+dr][c+dc] in '.1234567890\n': good=True
                except:
                    continue

print(s)       

gears=defaultdict(list)
adj=set()
num=0
for r in range(rows):
    for c in range(cols):
        ch = lines[r][c]
        if not ch in '1234567890':
            if not len(adj) == 0:
                for ad in list(adj):
                    gears[ad].append(num)

            adj.clear()
            num=0
            continue
        
        if ch.isdigit():
            num = 10*num + int(ch)

            for dr,dc in zip(Dr,Dc):
                try:
                    if lines[r+dr][c+dc] == '*': adj.add((r+dr,c+dc))
                except:
                    continue

# print(gears)         
s=0
for ad in gears:
    if len(gears[ad]) == 2:
        s+=gears[ad][0]*gears[ad][1]

print(s)
