l = [-10, 55, 2, 3, 4, -1, 2]

for i in range(0, len(l) - 1):
    mn = l[i]
    p = i 
    for j in range(i + 1, len(l)):
        if mn > l[j]:
            mn = l[j]
            p = j
    
    t = l[i]
    l[i] = l[p]
    l[p] = t

print(l)  