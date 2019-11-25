a=input()
a=a.replace(' ','')
x=1
b=0
for i in range (len(a)//2):
        if a[i]==a[-x]:
            x+=1
        else:
            b=1
            break
if b==0:
    print("YES")
else:
    print("NO")
