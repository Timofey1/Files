a=input().upper()
a=a[0:a.find('.')]
out=[]
for i in a:
    if 64<ord(i)<91:
        out.append(i)
out.sort()
m=max(out, key=out.count)
z=out.count(m)
print(m,z)