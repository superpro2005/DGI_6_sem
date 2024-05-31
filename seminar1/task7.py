#months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
#'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#for month in months:
 #print(month)

a = [1,1,1,1,0,0,0,1,0,0,1,1,0,1,0]
for i in range(15):
    if a[i] == 1:
        a[i] = -1
    if a[i] == 0:
        a[i] = 1
b = a
c = a
d =a
print (a)
n = 15
sum1 = 0
k = 0
l=14
for k in range(n):
    for i in range(l):
        sum1= sum1 + b[i]*c[k]
    del c[k]
    l=l-1
    print(sum1," next")
    print(k)
    n=n-1
