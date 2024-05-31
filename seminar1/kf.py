a = [1,1,1,1,0,0,0,1,0,0,1,1,0,1,0]
for i in range(a):
    if a[i] == 1:
        a[i] = -1
    if a[i] == 0:
        a[i] = 1
print (a)