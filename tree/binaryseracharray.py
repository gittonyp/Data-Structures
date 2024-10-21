arr=[1,2,3,4,5,6,7]
i=0
j=len(arr)-1
target=6
while i<j:
    middle=((j-i)//2)+i
    if target==arr[middle]:
        print(f"index {middle}")
        break
    if target>arr[middle]:
        i=middle
    else:
        j=middle


        