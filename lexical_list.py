x = 2
y = 3
z = 4
n = 4
ar = []
p = 0
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i+j+k != n:
                ar.append([])
                ar[p] = [i, j, k]
                print('x=', i, 'y=', j, 'z=', k)
                p += 1
print(ar)