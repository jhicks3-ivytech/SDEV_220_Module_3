"""
John Hicks
Module 3 Lab - Case Study: Lists, Functions, and Classes
1/29/2025
This script defines a parent class for Vehicle and it's more detailed child class 
Automobile. The use of the function build_automobil() gives the ability to prompt 
user for inputs and checks for constraints. 
"""

class Vehicle:
    def __init__(self,type):
        #Initiates the class attributes
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        #Initiates the class attributes
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def __str__(self):
        #Defines the string representation of the class
        return (f"Type: {self.type}\n"
                f"Year: {self.year}\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Doors: {self.doors}\n"
                f"Sunroof: {self.roof}\n")
        


def build_automobile():
    #Assign this function to a variable to create an instance of Automobile.
    #Collects user input as arguments for the class parameters.
    type = input("Vehicle type: ").capitalize()
    year = int(input("Year: "))
    make = input("Make: ").capitalize()
    model = input("Model: ").capitalize()
    while True:
        #Ensures proper input for door count
        doors = input("2 or 4 doors: ")
        if doors in ('2', '4'):
            doors = int(doors)
            break
        else:
            print("Not 2 or 4. Try again: ")
    while True:
        #Ensures proper input for the sunroof
        roof = input("Sunroof Y/N: ")
        if roof.upper() in ('Y', 'TRUE', 'YES'):
            roof = True
            break
        elif roof.upper() in ('N',"FALSE", "NO"):
            roof = False
            break
        else:
            print("Response not recognized, try again")
    return Automobile(type, year, make, model, doors, roof)

automobile1 = build_automobile()
print("Automobile Details\n" + str(automobile1))