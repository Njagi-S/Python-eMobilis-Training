#Int
number = 25

#Float
second = 56.78

#String
text="Hello There"

#Boolean
isPythonInteresting = True


#DATA STRUCTURES - Multiple  values stored in a single variable
cars=["toyota","nissan","vw"] #List - ordered and changeable
fruits = ("Banana","Orange","apple") #Tuple - Ordered but unchangeable
countries={"Kenya","Tunisia","Algeria"} #Set - Unordered and mutable
student = {
    "Firstname":"Sheldon",
    "Lastname":"Njagi",
    "Age":24,
    "Course":"Web Development",
    "Nationality":"Kenyan"
} # Dictionary - Key and Value Pair


print(cars)
print(fruits)
print(countries)
print(student)

#To Know which type of datatype
print(type(cars))
print(type(fruits))
print(type(countries))
print(type(student))
print(type(text))
print(type(isPythonInteresting))
print(type(number))
print(type(second))

#Accessing data in a dictionary
print(student["Firstname"]) #acceses the firstname using the key


print(number)
print(second)
print(text)
print(isPythonInteresting)

#Typecasting - Process of converting from one datatype to another
#converting an integer to a float
print(float(number))

#converting a float to an integer
print(int(second))