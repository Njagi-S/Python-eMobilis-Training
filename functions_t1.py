# Reusable block of code
# 2 Types --- (1). Built-in  Library Functions --- and --- (2). User-Defined Functions ---

# (1). --- Built-in Library Functions ---
# Maximum Value
y = max(56,78,90,23,12)
print("The maximum value is",y)

# Minimum Value
x = min(67,10,45,32,76)
print("The minimum value is " + str(x))

# Power (Exponents)
z = pow(2,3) # 2**3
print("The result of 2 to power 3 is : " + str(z))

# (2). --- User-Defined Functions
def greeting():
    print("Hello There !")

greeting()

# Returning the product of two numbers
def multiply():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print("The result is",num1*num2)

multiply()
# Parameters/Variables and Arguments/Values
# Returning the sum of two values
def sum1(a,b,c):
    print("The sum is:",a+b+c)

sum1(31,64,97)
sum1(46,14,57)
sum1(35,43,76)


# Functions to display employee details
def employee(fullname,age,position,marital_status):
    print(fullname,age,position,marital_status)
employee("Mark Joe",34,"Junior Developer","Single")
employee("Mellisa Joe",44,"Senior Developer","Married")
employee("Mary Job",27,"HR Manager","Single")
employee("John Doe",51,"C.E.O","Married")