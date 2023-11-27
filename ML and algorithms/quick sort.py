from random import randint

lenght = int(input())
if lenght == 0:
    exit()
arr = list(map(int, input().split()))


def quick_sort(array):
    leng = len(array)
    if leng <= 1:
        return array
    else:
        partition = randint(0, leng - 1)
        pivot = array[partition]
        G = 0
        E = 0
        for i in range(leng):
            if array[i] < pivot:
                array[i], array[G], array[E] = array[G], array[E], array[i]
                E += 1
                G += 1
            elif array[i] == pivot:
                array[G], array[i] = array[i], array[G]
                G += 1
        return quick_sort(array[:E]) + array[E:G] + quick_sort(array[G:])


sort = quick_sort(arr)
print(*sort)
