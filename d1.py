
s=0
with open('d1_in.txt','r') as f:
    for l in f.readlines():
        for c in l:
            if c.isdigit():
                s+=10*(int(c))
                break
    
        for c in l[::-1]:
            if c.isdigit():
                s+=int(c)
                break

print(s)

s=0

with open('d1_in.txt','r') as f:
    for l in f.readlines():
        lm=l.replace('one','one1one').replace('two','two2two').replace('three','three3three').replace('four','four4four').replace('five','five5five').replace('six','six6six').replace('seven','seven7seven').replace('eight','eight8eight').replace('nine','nine9nine')
        
        for c in lm:
            if c.isdigit():
                s+=10*(int(c))
                break
    
        for c in lm[::-1]:
            if c.isdigit():
                s+=int(c)
                break

print(s)