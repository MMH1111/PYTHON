first_name = "Bob"
last_name = "Ross"
age = 35

fstring = f"Hi, my name is {first_name}"

print(first_name)

print(f"Hi my name is {first_name} {last_name} and I am {age}!")

print(fstring)

print("-" * 25)

if age > 40:
    print("Over 40")
elif age > 30:
    if age > 35:
        print("Over 35")
    else:
        print("under 35")
    if first_name == "Bob":
        print("Hi Bob")
    print("Between 30 & 40")
else:
    print("Less than 30")

print("-" * 25)

for i in range(1, 7): #For loop. In parentheses, the first is the starting number (inclusive), the 2nd is the ending one exclusive, the 3rd specifies the count
    print(i)

namelist = ["Max", "Christian", "Alejandro"]

print("-" * 25)

for i in range(0, len(namelist)):
    print(namelist[i])

print("-" * 25)

for name in namelist:
    print(name)

print("-" * 25)

my_int = 0
while my_int < 10:
    print(my_int)
    my_int += 1 #

print("-" * 25)

def my_function(): #defined the function
    print("Hello from the function")

my_function() #calling the function

print("-" * 25)

def say_hello(name): #how to pass in parameters in functions
    print(f"Hello {name}!")

say_hello("Armando")

print("-" * 25)

def say_hello(name): 
    print(f"Hello {name}!")

name = "Armando"

say_hello(name)

name = "Christian"

say_hello(name)

print("-" * 25)

def say_hello(name): 
    print(f"Hello {name}!")

name_list = ["Armando", "Max", "Christian", "Sabrina"]

def print_names(names):
    for name in names:
        if name != "Christian":
            print("Hello {name}")

print_names(name_list)