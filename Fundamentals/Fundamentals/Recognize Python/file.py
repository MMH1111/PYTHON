# const num1 = 45 #how it would be done in JavaScript. Using const keyword.
num1 = 42 # variable declaration, initialize integer
num2 = 2.3 # variable declaration, initialize integer
boolean = True # boolean variable declaration, initialize to true
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list declaration, initialize (called array in JS, but it's a list in python)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary declaration with key value pairs
fruit = ('blueberry', 'strawberry', 'banana') #list declaration
print(type(fruit)) #call function called type with fruit argument
print(pizza_toppings[1]) #call function called pizza_toppings with index of 1 argument
pizza_toppings.append('Mushrooms') #add/append 'Mushrooms' to pizza_toppings function
print(person['name'])  #add/append 'Mushrooms' to pizza_toppings function
person['name'] = 'George'  #changing array value name to George
person['eye_color'] = 'blue' #changing array value eye_color to blue
print(fruit[2]) #calling function called fruit index 2

if() #how it'd be done in JS
if num1 > 45: #if conditional
    print("It's greater")
else: #else conditional
    print("It's lower")

if len(string) < 5: #if conditional using operation length with string variable
    print("It's a short word!") 
elif len(string) > 15: #else if conditional
    print("It's a long word!")
else: #else conditional
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop
    print(x)
for x in range(2,10,3): #for loop
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #remove last index item from array
pizza_toppings.pop(1) #remove index item 1 from array

print(person) #output person variable
person.pop('eye_color') #remove eye_color from person variable
print(person) #output person variable

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if conditional
        continue
    print('After 1st if statement')
    if topping == 'Olives': #if conditional
        break

def print_hello_ten_times(): #function named print_hello_ten_times with no parameters passed
    for num in range(10): #for loop within function
        print('Hello')

print_hello_ten_times() #calling the function named print_hello_ten_times

def print_hello_x_times(x): #function named print_hello_x_times with x as parameter passed
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #calling the function named print_hello_x_times with 4 as argument passed

def print_hello_x_or_ten_times(x = 10): #calling the function named print_hello_ten_times
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()  #calling the function named print_hello_x_or_ten_times
print_hello_x_or_ten_times(4) #calling the function named print_hello_x_or_ten_times with 4 as argument passed


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)