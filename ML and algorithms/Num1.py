x = int(input())
a = 1
b = 2
c = 0
while x != 0:
    if a**2 < b**3:
        c = a**2
        a += 1
        x -= 1
    elif a**2 == b**3:
        c = a**2
        a += 1
        b += 1
        x -= 1
    else:
        c = b**3
        b += 1
        x -= 1

print(c)