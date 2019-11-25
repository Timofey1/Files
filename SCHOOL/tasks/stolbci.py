x = int(input())
n = int(input())
m = ["NO"]*n


for i in range(n):
    r = input().split()
    for o in range(len(r)):
        r[o]=int(r[o])


    for j in range(len(r)):
        if r[j]==x:
            m[j]="YES"
for h in range(len(m)):
    print(m[h])