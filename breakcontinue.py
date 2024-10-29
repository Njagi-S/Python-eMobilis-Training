# Break Statement _ Exits the entire loop

num = int(input("Enter your number: "))
while num <= 25:
    print(num)
    if num ==23:
        break
    num +=1

# Continue statement - Skips a loop
devices = ["laptop","phone","tablet"]
for x in devices:
    if x == "phone":
        continue
    print(x)