def staircase(n):
    print('Start ...')
    for i in range(n):
        str_form = '{:>' + str(n-i-1) + '}{:#<' + str(i+1) + '}'
        print(str_form.format('', ''))

if __name__ == '__main__':
    n = 6
    staircase(n)