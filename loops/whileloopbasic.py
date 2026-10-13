#print first n natural numbers
n=int(input())
i=1
while(i<=n):
    print(i)
    i+=1
#print natural numbers in reverse
n=int(input())
i=n
while(i>0):
    print(i)
    i-=1
#all even numbers from 1 to n
n=int(input())
i=0
while(i<=n):
    if(i%2==0):
        print(i)
    i+=1
#all odd numbers from 1 to n
n=int(input())
i=0
while(i<=n):
    if(i%2 != 0):
        print(i)
    i+=1
#multiples of 5 from 5 to 50
i=1
while(i<=50):
    if(i%5==0):
        print(i)
    i+=1
#multiplication table of a number 
n=int(input())
i=1
while(i<=10):
    print(f"{n} * {i}=",n*i)
    i+=1
#sum of num from 1 to n
n=int(input())
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1
print(sum)
#count num printed from 1 to n
n=int(input())
i=1
count=0
while(i<=n):
    print(i)
    count+=1
    i+=1
print(f"The count of numbers  printed from 1 to {n} = ",count)

#factorial of a number
n=int(input())
fact=1
i=0
while(i < n):
    fact=fact*(n-i)
    i+=1
print(fact)