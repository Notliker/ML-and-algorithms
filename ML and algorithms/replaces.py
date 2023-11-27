n = int(input())
arr = list(map(lambda num: num+1, range(n)))
res=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j:
            arr[i],arr[j]=arr[j],arr[i]
            print(arr)
            arr[i],arr[j]=arr[j],arr[i]
