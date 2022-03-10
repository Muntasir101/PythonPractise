import random

a = []
b = []
for x in range(0, 10):
    a.append(random.randint(0, 20))
    b.append(random.randint(0, 20))
a.sort()
b.sort()

print(a, '\n', b, '\n')
print(list(dict.fromkeys([i for i in a if i in b])))
