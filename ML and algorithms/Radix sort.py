num = int(input())
arr = []
for i in range(num):
    arr.append(input())
print("Initial array:")
print(*arr, sep=", ")


def radix_sort(arr):
    nums = [[] for _ in range(10)]
    for j in arr:
        nums[int(j[-1 * i])].append(j)

    for x in range(len(nums)):
        print(f"Bucket {x}: {', '.join(nums[x]) if nums[x] else 'empty'}")

    return [nums[q][_] for q in range(10) for _ in range(len(nums[q]))]


for i in range(1, len(arr[0]) + 1):
    print("**********")
    print(f"Phase {i}")
    arr = radix_sort(arr)
    print(arr)
print("**********")
print("Sorted array:")
print(*arr, sep=", ")
