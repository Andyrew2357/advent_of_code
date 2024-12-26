import numpy as np
import re

s1 = 0
s2 = 0

with open('d4_in.txt', 'r') as f:
    Ch = np.array([list(s.strip()) for s in f.readlines()], dtype=str)

N, M = Ch.shape

for i in range(N):
    l = ''.join(Ch[i,:])
    s1+=len(re.findall(r'XMAS', l)) + len(re.findall(r'SAMX', l))

for i in range(M):
    l = ''.join(Ch[:,i])
    s1+=len(re.findall(r'XMAS', l)) + len(re.findall(r'SAMX', l))

for i in range(-N+1,N):
    l = ''.join(np.diagonal(Ch, i))
    s1+=len(re.findall(r'XMAS', l)) + len(re.findall(r'SAMX', l))

Ch = np.flip(Ch, axis=0)
for i in range(-N+1,N):
    l = ''.join(np.diagonal(Ch, i))
    s1+=len(re.findall(r'XMAS', l)) + len(re.findall(r'SAMX', l))

print(s1)

for r in range(1, N-1):
    for c in range(1, M-1):
        if not Ch[r, c] == 'A': continue

        A = (Ch[r-1, c-1], Ch[r+1, c+1]) in [('M', 'S'), ('S', 'M')]
        B = (Ch[r-1, c+1], Ch[r+1, c-1]) in [('M', 'S'), ('S', 'M')]
        
        if A and B: s2+=1

print(s2)
