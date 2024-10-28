# While loop

# Increment
number = int(input("Enter a number: "))
while number<= 20:
    print(number)
    number += 1

# Decrement
count = int(input("Enter a number: "))
while count >= 100:
    print("Number is",count)
    count -= 1

# For Loop
for x in range(10):
    print(x)

for num in range(15, 20):
    print(num)

for b in range(1,10,2):
    print(b)

languages=["Python","PHP","Kotlin"]
for lang in languages:
    print(lang)