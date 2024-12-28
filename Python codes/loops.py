print("In this program we are going to use loops")
i=1
while i<=100:
    print(i)
    i+=1
print("\ndone")
i-=1
while i>=1:
    print(i)
    i-=1
print("\ndone")

x = int(input("Enter a number "))
j=1
while j<=10:
    print(x,"X",j,"=",x*j )
    j+=1

list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<len(list):
    print(list[i])
    i+=1

tuple = (1,4,9,16,25,36,49,64,81,100)
input = int(input("enter the no. to be searched "))
i=0
while i<len(tuple):
   if tuple[i] == input:
    print("Index of the given no. is",i)

   i+=1