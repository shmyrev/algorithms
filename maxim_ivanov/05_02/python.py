n = int(input())
f = [0, 1]
while len(f) <= n:
    f.append(f[-1] + f[-2])
print(f[n])