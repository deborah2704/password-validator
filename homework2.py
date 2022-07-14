# Exercise 1.a
s = "abaaacccddehhsssshaaff"
cnt = {}
for ch in s:
    if ch not in cnt.keys():
        cnt[ch] = 1
    else:
        cnt[ch] += 1
d1 = dict(sorted(cnt.items()))
print("Exercise 1.a")
print(d1)

# Exercise 1.b
d2 = {}
for a, b in d1.items():
    if d2.get(b) is None:
        d2[b] = []
    d2[b].append(a)
print("Exercise 1.b")
print(d2)

# Exercise 2.a
l1 = [11, 7, 5, 8, 5, 37, 11, 5]
s1 = set()
for v in l1:
    if l1.count(v) > 1:
        s1.add(v)
print("Exercise 2.a")
print(s1)

# Exercise 2.b
list1 = [22, 8, 10, 1, 11, 22]
list2 = [71, 3, 22, 8, 2, 14, 1]
set1 = set()
for number in list1:
    if number in list2:
        set1.add(number)
list3 = list(set1)
print('Exercise 2.b')
print(list3)

# Exercise 3
list1 = [31, 99, 3, 1943, 7]
sort_order = 'asc'

list2 = []
for number in list1:
    for digit in str(number):
        if int(digit) not in list2:
            list2.append(int(digit))
if sort_order == 'desc':
    list2.sort(reverse=True)
else:
    list2.sort()

print('Exercise 3')
print(list2)
