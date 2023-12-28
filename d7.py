import functools

with open('d7_in.txt', 'r') as f:
    slines = [(l.split()[0],int(l.strip().split()[1])) for l in f.readlines()]
    hand = [a for (a,b) in slines]
    bid = {a:b for (a,b) in slines}

def find_type(a):
    chs = dict()
    for ch in a:
        if not ch in chs: 
            chs[ch] = 1
        else:
            chs[ch]+=1

    if len(chs) == 1: return 1
    if len(chs) == 2:
        if chs[a[0]] in [1,4]: return 2
        return 3
    if len(chs) == 3:
        if max([chs[k] for k in chs]) == 3: return 4
        return 5
    if len(chs) == 4: return 6
    return 7

cds = 'AKQJT98765432'
def hand_order(a,b):
    if a == b: return 0
    ta, tb = find_type(a), find_type(b)
    if ta < tb: return 1
    if ta > tb: return -1

    for i in range(5):
        cha, chb = cds.index(a[i]), cds.index(b[i])
        if cha < chb: return 1
        if cha > chb: return -1

hand.sort(key=functools.cmp_to_key(hand_order))
print(sum([(i+1)*bid[hand[i]] for i in range(len(hand))]))

# part 2 mostly copy pasted from part 1

def find_type(a):
    chs = dict()
    j=0
    for ch in a:
        if ch =='J':
            j+=1
            continue
        if not ch in chs: 
            chs[ch] = 1
        else:
            chs[ch]+=1
    if len(chs) == 0: return 1
    best=max(chs, key=lambda x: chs[x])
    chs[best]+=j

    if len(chs) == 1: return 1
    if len(chs) == 2:
        if max([chs[k] for k in chs]) == 4: return 2
        return 3
    if len(chs) == 3:
        if max([chs[k] for k in chs]) == 3: return 4
        return 5
    if len(chs) == 4: return 6
    return 7

cds = 'AKQT98765432J'
def hand_order(a,b):
    if a == b: return 0
    ta, tb = find_type(a), find_type(b)
    if ta < tb: return 1
    if ta > tb: return -1

    for i in range(5):
        cha, chb = cds.index(a[i]), cds.index(b[i])
        if cha < chb: return 1
        if cha > chb: return -1

hand.sort(key=functools.cmp_to_key(hand_order))
print(sum([(i+1)*bid[hand[i]] for i in range(len(hand))]))