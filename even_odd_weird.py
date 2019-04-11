N = 3
if N % 2 != 0:
    print('Weird')
else:
    if N % 2 == 0 and N in range(2, 5):
        print('Not Weird')
    if N % 2 == 0 and N in range(6, 20):
        print('Weird')
    if N % 2 == 0 and N > 20:
        print('Not Weird')