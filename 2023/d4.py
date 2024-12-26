s=0
with open('d4_in.txt','r') as f:
    for l in f.readlines():
        win,hand=l.strip().split('|')
        win=set([int(e) for e in win.split()[2:]])
        hand=set([int(e) for e in hand.split()])

        if win.intersection(hand): s+=2**(len(win.intersection(hand))-1)

print(s)

with open('d4_in.txt','r') as f:
    cards=f.readlines()

from collections import defaultdict

dct=defaultdict(int)

for i,l in enumerate(cards):
    dct[i]+=1
    N=dct[i]
    win,hand=l.strip().split('|')
    win=set([int(e) for e in win.split()[2:]])
    hand=set([int(e) for e in hand.split()])
    matches=len(win.intersection(hand))

    if not matches==0:
        for j in range(i+1,i+matches+1):
            dct[j]+=N

s=sum([dct[u] for u in range(len(cards))])
print(s)
