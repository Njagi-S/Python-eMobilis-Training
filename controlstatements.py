temperature = int(input('Enter your temperature: '))

if temperature > 20:
    print("It is too hot")
else:
    print("It is too cold")

# A python program to check 3 numbers and return the smallest number

num1=int(input('Enter your first number: '))
num2=int(input('Enter your second number: '))
num3=int(input('Enter your third number: '))

if num1<num2 and num1<num3:
    print("Number one is the smallest number:",num1)
elif num2<num3 and num2<num1:
    print("Number two is the smallest number:",num2)
else:
    print("Number three s the smallest number:",num3)


# A python program to check 3 numbers and return the largest number

num14=int(input('Enter your first number: '))
num12=int(input('Enter your second number: '))
num13=int(input('Enter your third number: '))

if num14>num12 and num14>num13:
    print("Number one is the largest number:",num14)
elif num12>num13 and num12>num14:
    print("Number two is the largest number:",num12)
else:
    print("Number three s the largest number:",num13)


# A program to check whether a number is even or odd
number = int(input('Enter your number: '))
if number % 2 ==0:
    print(number,"is an even number")
else:
    print(number,"is an odd number")