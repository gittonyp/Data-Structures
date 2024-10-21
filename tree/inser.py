def swap(i,j,arr):
    b=arr[i]
    arr[i]=arr[j]
    arr[j]=b
    return arr
arr=[3,30,20,15,10,8]

# bubbule
for i in range(len(arr)):
    j=i-1
    k=i
    while(j>0):
        if arr[k]>arr[j]:
            arr=swap(k,j,arr)
            k=k-1
        j=j-1
        


print(arr)