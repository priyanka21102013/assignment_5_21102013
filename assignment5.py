# Question 1
# To reverse the given string

# We take string as input from the user
s = input("Enter a string")
l = len(s)
s2 = ''
for i in range (l-1,-1,-1):
    s2 = s2+s[i] #Concatenating chracters starting from the back of the input string
    print("Reversed string is",s2)

# Enter a string priyanka
# Reversed string is a
# Reversed string is ak
# Reversed string is akn
# Reversed string is akna
# Reversed string is aknay
# Reversed string is aknayi
# Reversed string is aknayir
# Reversed string is aknayirp


# Question 2
# To print numbers in a given range divisible by a number

# We take range of number as input from the user
x1,x2 = input("Enter the range of number").split
x1 = int(x1)
x2 = int(x2)
n = int(input("Enter number"))
for i in range(x1,x2,1):
    if i%n==0: #If it is divisible print the number
        print(i)
        continue

# Question 3
# Area of a triangle

import math
a = int(input("Enter first side of the triangle"))
b = int(input("Enter second side of the triangle"))
c = int(input("Enter third side of the triangle"))
if a<0 or b<0 or c<0:
    print("Invalid input, side cannot be negative")
elif a+b<c or b+c<a or c+b<a:
    print("Combination of sides is not possible")
else:
    s =(a+b+c)/2 # Calculating semi perimeter
    area = math.sqrt(s*(s-a)*(s-b)*(s-c)) # Heron's formula
    print(f"Area of the triangle is {area}")
    print()

# Enter first side of the triangle6
# Enter second side of the triangle9
# Enter third side of the triangle7
# Area of the triangle is 20.97617696340303


# Question 4
# To print the star pattern
rows = 5
# outer loop will print the number of rows
for i in range(0,rows):
    # inner loop will print the stars
for j in range(0,i+1):
    print("*",end='')
    # Changing line after each iteration
    print()
# for second pattern
for i in range (rows,0,-1):
    for j in range(0,i-1):
        print("*",end='')
        print()


# Question 5
# To print pattern

rows = int(input("Enter the no of rows"))
m = 65 #ASCII code of A is 65
for i in range(rows):
    for j in range(i+1):
        if m>90:
            m=65
            print(chr(m),end='')
            m+=1
            print()
        print()


# Question 6
# To print  prime numbers in a given range

# We take range of numbers as input from the user
x1,x2 = input("Enter the range of numbers").split()
x1 = int(x1)
x2 = int(x2)
for i in range (x1,x2,1):
    c=0
    n=1
    while n<=i:
        if i%n==0:
            c+=1
            n+=1
            continue
            n=n+1
            if c==2:
                print(i)
                print()


#Question 7
# To print numbers that are multiple of 7 and divisible by 11 in the range 1-500
for i in range(1,500):
    if i%7==0 and i%11==0
        print(i)
print()

# Question 8
list [] # We take an empty list to store the integer values input by the user
for i in range(0,10,1):
    n=int(input(f"Enter {i+1} number"))
    list.append(n)
    print(list)

    #a
    print("positive number are")
    for i in range (10):
        if list[i]>0:
            print(list[i])


    #b
    print("Negative numbers are")
    for i in range(10):
        if list[i]<0:
            print(list[i])

    #c
    print("odd numbers are")
    for i in range(10):
        if list[i]%2!=0:
            print(list[i])


    #d
    print("Even number are")
    for i in range(10):
        if list[i]%2==0
            print(list[i])

    #e
    count=dict()
    for no in list:
        if no in count:
            count[no]+=1
        else:
            count[no]=1
            print("No of times each number occurs in the list")
            print(count)
            print()


# Question 9
# count the number of occurrence of each word in the list input by the user
str=input("Enter a string")
#Empty dictionary is created to
counts = dict()
#We split the input string into words and store it in a list
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        count[word] = 1

print(counts)


