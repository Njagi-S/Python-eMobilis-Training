try:
    print(number)
except:
    print("An Error has occurred")


num1 = 39
num2 = 0

try:
    print(num1/num2)
except:
    print("A ZeroDivisionError has occurred")
finally:
    print("Success")