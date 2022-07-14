lst = [1,2,3]
lst2 = []

for item in lst:
    res = str("*"*item)
    lst2.append(res)
print(lst2)


a = [1,2,3]
b = [3,2,1]
c = []
le = len(a)

for item in range(le):
    r = str(a[item]) + str(b[le-item-1])
    c.append(int(r))
print(c)
