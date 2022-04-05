n = int(input("별 찍기 : "))

for i in range(1, n + 1):
    for space in range(n - i, 0, -1):
        print(' ', end='')

    for star in range(1, 2 * i):
        print('*', end='')
    print()
