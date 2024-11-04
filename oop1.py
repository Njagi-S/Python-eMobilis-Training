class student:
    #Properties/Variables/Characteristics/Attributes
    name ="Joe"
    age = 21

    #Behaviours/Methods/FUnctions
    def study(self):
        print("Student is studying")

student1 = student() # Instantiating/Creating an Object
student1.study()

print(student1.name)