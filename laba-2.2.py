n = int(input("число n: "))

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')

    for j in range(i, 0, -1):
        print(j, end='')

    for e in range(2, i + 1):
        print(e, end='')

    print()
