import numpy as np

with open('d13_in.txt', 'r') as f:
    lines = f.read().splitlines()

def eval(im):
    R, C = im.shape
    for r in range(1,R):
        if np.array_equal(im[max(0,2*r-R):r,:],np.flip(im[r:min(2*r,R),:], axis = 0)): return 100*r
    
    for c in range(1,C):
        if np.array_equal(im[:,max(0,2*c-C):c],np.flip(im[:,c:min(2*c,C)], axis = 1)): return c

    return 0

def eval2(im):
    R, C = im.shape
    for r in range(1,R):
        if np.where((im[max(0,2*r-R):r,:] == np.flip(im[r:min(2*r,R),:], axis = 0)) == False)[0].size == 1: 
            return 100*r
    
    for c in range(1,C):
        if np.where((im[:,max(0,2*c-C):c] == np.flip(im[:,c:min(2*c,C)], axis = 1)) == False)[0].size == 1: 
            return c

    return 0

s1, s2 = 0, 0
im = []
for i, l in enumerate(lines):
    if not l == '':
        im.append([c for c in l])
        continue
    
    s1+=eval(np.array(im))
    s2+=eval2(np.array(im))
    im = []

s1+=eval(np.array(im))
s2+=eval2(np.array(im))
print(s1)
print(s2)
