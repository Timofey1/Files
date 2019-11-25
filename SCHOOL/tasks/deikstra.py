def dijkstra(s):
    global a, d, used
    used[s] = True # посещённая вершина
    for i in range(n):
        if a[s][i] != -1:
            if d[i] == -1 or d[i] > d[s] + a[s][i]: #через вершину быстрее, чем раньше
                d[i] = d[s] + a[s][i]
    m = -1 # вершина, ближайшая к s
    for i in range(n):
        if d[i] != -1:
            if not used[i]:
                if m == -1 or d[i] < d[m]:
                    m = i
    if m != -1:
        dijkstra(m)

n, s, f = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

d = [-1 for i in range(n)]
d[s - 1] = 0
used = [False for i in range(n)]

dijkstra(s - 1)
print(d[f - 1])