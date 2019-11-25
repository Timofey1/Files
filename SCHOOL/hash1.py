def hash(a,t):
    s=0
    for i in range(len(a)):
        s=s+ord(a[i])

    return s%t

x=hash('haguhausp', 13)

print(x)
