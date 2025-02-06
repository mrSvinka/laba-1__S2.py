n = int(input("число n: "))
d = 1
u = 0
r = 0
y = 1
h = 0
#нашли число для целочисленного деления
while u <= n:
    if n // d >= 10:
        d *= 10
    else:
        if 0 < n // d < 10:
            u = d
            break
print(u)
# нашли кол-во нулей в числе
while u>=y:
    if u // y >= 10:
        y *= 10
        r += 1
    else:
        if 0 < u // y < 10:
            r += 0
            break
print(r, y)



for i in range(n, 0, -1):
    while i>0:
        if 0 >= i // u:
            u /= 10
            r -= 1

        else:

            if 0 < i // u < 10:
                h+=r
                print((' ' * (n + r - i)), end='')





    for j in range(i, 0, -1):
        print(j, end='')

    for e in range(2, i + 1):
        print(e, end='')

    print()



