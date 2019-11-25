n, s = map(int,input().split())
arr = [int(i) for i in input().split()]
res = [0]*(100000)

for i in range(0,n):
    for j in range(s,0,-1):
        if res[j]!=0:
            if res[j+arr[i]] != 0:
                res[j+arr[i]] = min(res[j+arr[i]], 1+res[j])
            else:
                res[j+arr[i]] = res[j] + 1
    res[arr[i]]=1
print(res[s])
