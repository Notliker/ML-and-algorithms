lent = int(input())
if lent == 0:
    exit()
arr = list(map(int, input().split()))
def merge_sort(array):
    lenght=len(array)
    arr1 = array[:lenght // 2]
    arr2 = array[lenght // 2:]
    res=[]
    if len(arr1) <= 1 and len(arr2) <= 1:
        return min(arr1, arr2)+max(arr1, arr2)
    else:
        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)
        pos1 = 0
        pos2 = 0
        while pos1 < len(arr1) and pos2 < len(arr2):
            if arr1[pos1] <= arr2[pos2]:
                res.append(arr1[pos1])
                pos1 += 1
            else:
                res.append(arr2[pos2])
                pos2 += 1
        res += arr1[pos1:] + arr2[pos2:]
        return res


sort = merge_sort(arr)
print(*sort)
