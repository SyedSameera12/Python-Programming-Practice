#num from 2 to 20 , inc by 2
n=int(input())
for i in range(0,n+1,2):
    print(i)

#num in custom range
start=int(input())
end=int(input())
for i in range(start,end+1):
    print(i)

# multiples of any number
n=int(input())
for i in range(1,11):
    print(f"the multiples of {n} * {i} =",n*i)

#countdown with message
print("The countdown starts in")
for i in range(1,6):
    print(i)
print("Blast off!!")

#calculating sum of squares
num=int(input())
sum=0
for i in range(1,num+1):
    sum=sum+(i**2)
print(sum)

#printing cubes from 1 to n
n=int(input())
for i in range(1,n+1):
    print(f"The cube value of {i}",(i*i*i))

# numbers divisible by 4
n=int(input())
for i in range(1,n+1):
    if(i%4==0):
        print(i)

#product of number from 1 to n
n=int(input())
product=1
for i in range(1,n+1):
    product*=i
print(product)

#each character in a word
word=input()
chr=''
for i in range(len(word)):
    chr=word[i]
    print(chr)

#Calculating total marks
n=int(input("Enter how many sub u have :"))
total=0
for i in range(1,n+1):
    print(f"enter the marks in sub {i}")
    marks=int(input())
    total+=marks
print( f"The total marks in {n} are",total)