#write a python program to check the entered number is prime or not
no=(int)(input("Enter The Number:"))
flag=0
if no>1:
    for i in range(2,no):
        if no%i==0:
            flag=1
            break
    else:
        print(f"the entered number is prime number")
else:
    print("entered number is not prime number")

if flag==1:
    print("entered number not prime number")