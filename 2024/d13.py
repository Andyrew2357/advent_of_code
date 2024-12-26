with open('d13_in.txt', 'r') as f:
    s1 = 0
    while True:
        l1 = f.readline().strip().split()
        if len(l1) == 0: break
        a11, a21 = int(l1[2][2:-1]), int(l1[3][2:])
        l2 = f.readline().strip().split()
        a12, a22 = int(l2[2][2:-1]), int(l2[3][2:])
        l3 = f.readline().strip().split()
        o1, o2 = int(l3[1][2:-1]), int(l3[2][2:])
        l4 = f.readline()

        D = a11*a22-a12*a21
        i1, i2 = (a22*o1-a12*o2)/D, (a11*o2-a21*o1)/D

        if not (int(i1) == i1 and int(i2) == i2): continue
        if i1 > 100 or i2 > 100: continue
        s1+=3*i1 + i2

print(int(s1))

#part 2
with open('d13_in.txt', 'r') as f:
    s2 = 0
    while True:
        l1 = f.readline().strip().split()
        if len(l1) == 0: break
        a11, a21 = int(l1[2][2:-1]), int(l1[3][2:])
        l2 = f.readline().strip().split()
        a12, a22 = int(l2[2][2:-1]), int(l2[3][2:])
        l3 = f.readline().strip().split()
        o1, o2 = int(l3[1][2:-1])+1e13, int(l3[2][2:])+1e13
        l4 = f.readline()

        D = a11*a22-a12*a21
        i1, i2 = (a22*o1-a12*o2)/D, (a11*o2-a21*o1)/D

        if not (int(i1) == i1 and int(i2) == i2): continue
        s2+=3*i1 + i2

print(int(s2))
