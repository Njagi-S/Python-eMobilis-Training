
courses = ["MIT","CyberSecurity","Datascience"]
print(courses)

#Accessing an element in an array
print(courses[0])   # For accessing MIT

# Looping through an array
for cs1 in courses:
    print("The available courses are:",cs1)

#Adding values to an array
courses.append("Android Development")
print(courses)

# Removing an element from an array
courses.remove("MIT")
print(courses)
# using pop method -- removes the last element (last in first out --LIFO)
courses.pop()
print(courses)
