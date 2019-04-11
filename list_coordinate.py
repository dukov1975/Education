x = 1
y = 1
z = 1
n = 2
ar = []
p = 0
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i+j+k != n:
                ar.append([])
                ar[p] = [i, j, k]
                p += 1
                print('x=', i, 'y=', j, 'z=', k)
print(ar)