string = input()
n = len(string)
p = 10 ** 9 + 7
x_ = 257
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
string = ' ' + string
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(string[i])) % p
    x[i] = (x[i - 1] * x_) % p
if n == 1:
    print(1)
    exit()
if n == 0:
    print(0)
    exit()
def isequal(from1, from2, slen):
    return (
        (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % p ==
        (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p
    )
ans = 0
for i in range(n):
    if isequal(1, n-i+1, i):
        ans = i
print(n-ans)

