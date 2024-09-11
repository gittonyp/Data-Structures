def intersection(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                print(list1[i])


def union(list1,list2):
    for i in range(len(list1)):
        print(list1[i])
    for i in range(len(list2)):
        n=0
        for j in range(len(list1)):
            if list1[j] == list2[i]:
                n=1
                break
        if n==0:
            print(list2[i])

def diff(list1,list2):

    for i in range(len(list1)):
        n=0
        for j in range(len(list2)):
            if list1[i] == list2[j]:  
                n=1
                break
        if n==0:
            print(list1[i])

def symdiff(list1,list2):

    for i in range(len(list1)):
        n=0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                n=1
                break
        if n==0:
            print(list1[i])
    for i in range(len(list2)):
        n=0
        for j in range(len(list1)):
            if list2[i] == list1[j]:
                n=1
                break
        if n==0:
            print(list2[i])


seta=[1,89,47,3,6,97,15]
setb=[1,96,37,58,63,2]
intersection(seta,setb)
print("\n")
union(seta,setb)
print("\n")
diff(seta,setb)
print("\n")
diff(setb,seta)
print("\n")
symdiff(seta,setb)