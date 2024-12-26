s = 0
with open('d2_in.txt', 'r') as f:
    for l in f.readlines():
        w=l.split(' ')
        id=int(w[1][:-1])
        
        poss=True
        for ind in range(2, len(w), 2):
            if 'red' in w[ind+1]:
                if int(w[ind]) > 12: poss = False
            elif 'blue' in w[ind+1]:
                if int(w[ind]) > 14: poss = False
            elif 'green' in w[ind+1]:
                if int(w[ind]) > 13: poss = False

        if poss:
            s+=id

print(s)

s=0
with open('d2_in.txt', 'r') as f:
    for l in f.readlines():
        w=l.split(' ')
        id=int(w[1][:-1])
        
        n_r, n_b, n_g = 0, 0, 0
        for ind in range(2, len(w), 2):
            if 'red' in w[ind+1]:
                if int(w[ind]) > n_r: n_r = int(w[ind])
            elif 'blue' in w[ind+1]:
                if int(w[ind]) > n_b: n_b = int(w[ind])
            elif 'green' in w[ind+1]:
                if int(w[ind]) > n_g: n_g = int(w[ind])

        s+=n_r*n_b*n_g

print(s)
