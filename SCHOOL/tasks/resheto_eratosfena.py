n = 100000
x = int(input())
a = [0] * n
for i in range(n):
    a[i] = i

a[1] = 0

m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
    m += 1

b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])

del a
print(b[x - 1])