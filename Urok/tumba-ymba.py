def gen(s):
	global cnt
	if (len(s) == n):
		print(s)
		cnt += 1
	else:
		if (s[-1] in gl):
			for j in sg:
				gen(s + j)
		else:
			for j in al:
				gen(s + j)

al = input()
n = int(input())
gl = []
cnt = 0
sg = []
for i in al:
	if (i in {'A', 'E', 'I', 'O', 'U'}):
		gl.append(i)
	else:
		sg.append(i)
for i in al:
	gen(i)
print(cnt)