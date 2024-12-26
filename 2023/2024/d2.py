import numpy as np

safe1 = 0
safe2 = 0
with open('d2_in.txt', 'r') as f:
    for L in f:
        a = np.array([int(i) for i in L.strip().split()])
        l = np.diff(a)
        if all(1 <= abs(i) <= 3 for i in l):
            if all(i < 0 for i in l) or all(i > 0 for i in l): safe1+=1

        for i in range(a.size):
            aa = np.delete(a, i)
            ll = np.diff(aa)
            if all(1 <= abs(i) <= 3 for i in ll):
                if all(i < 0 for i in ll) or all(i > 0 for i in ll): 
                    safe2+=1
                    break

print(safe1)
print(safe2)