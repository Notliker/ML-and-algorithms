N, M = map(int, input().split())
Arr = sorted(list(map(int, input().split())))
count = [2] * M
substr = []


def bricks(Arr, count, substr, N):
    if count[0] != 0 and N >= Arr[-1]:
        substr.append(Arr[-1])
        count[-1] -= 1
        N -= Arr[-1]
        if  bricks(Arr, count, substr, N) == 0:
            bricks(Arr[:-1], count[-1], substr, N)
    if count[0] == 0 and N != 0:
        return 0


for i in range(len(Arr), 1, -1):
    bricks(Arr[:i], count[:i], substr, N)
print(substr)
