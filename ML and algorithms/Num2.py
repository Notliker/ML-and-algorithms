n = int(input())
string = input()
p = 10**9+7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
h_reverse = [0] * (n + 1)
x[0] = 1
string = ' ' + string
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(string[i])) % p
    h_reverse[i] = (h_reverse[i - 1] * x_ + ord(string[-i])) % p
    x[i] = (x[i - 1] * x_) % p
if n == 1:
    print(0)
    exit()
if n == 0:
    print()
    exit()
def isequal(f1, f2, l):
    return (
            (
                    h[f1 + l - 1] + h_reverse[f2 - 1] * x[l]) % p ==
            (h_reverse[f2 + l - 1] + h[f1 - 1] * x[l]) % p
    )
res = [0] * n
for i in range(1, n+1):
    left = 0
    right = n + 2 - i
    while left < right:
        middle = (left + right) // 2
        if isequal(1, i, middle):
            left = middle + 1
        else:
            right = middle
    res[i - 1] = left - 1

if string:
    print(*reversed(res))
else:
    print()
