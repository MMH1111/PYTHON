# #1
# def number_of_food_groups():
#     return 5 #The function becomes what is returned
# print(number_of_food_groups())
# #Prediction: will print 5

#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Prediction: will return error because number_of_days_in_a_week_silicon_or_triangle_sides() is not defined

# #3
# def number_of_books_on_hold():
#     return 5 #a return statement always ends the function
#     return 10 #this is called unreachable code
# print(number_of_books_on_hold())
#Prediction: will print 5 because the first return statement will execute out of the function

# #4
# def number_of_fingers():
#     return 5
#     print(10) #another instance of unreachable code
# print(number_of_fingers())
#Prediction:  will print 5 because the first return statement will execute out of the function

# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes() #making the function call on this line then assigning that to x variable
# print(x)
#Prediction: will print 5 and then none because nothing was returned in the function so x doesn't have a value

#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
#Prediction: will print 3, 5, then error because can't add NoneTypes

# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))
#Prediction: will print 25 as a concatenated string

# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10 #this will return because 100 > 10
#     return 7 #unreachable code
# print(number_of_oceans_or_fingers_or_continents())
#Prediction: will print 100, 10

# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3 #unreachable code
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
    # Is 2<3? --> yes, so 7 will print in the console
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
    # Is 5<3? --> no, so 14 will print in the console
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
    # 21 will print in the console, because 7+14=21
#Prediction: will print 7, 14, 21

# #10
# def addition(b,c):
#     return b+c
#     return 10 #unreachable code
# print(addition(3,5))
#Prediction: will print 8, 3+5

# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b) #Lines 83-85 don't run until foobar function is called on line 87
# print(b)
# foobar()
# print(b)
#Prediction: will print 500(print(b)), 500(print(b)), 300(foobar), 500(print(b))

# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b #lines 94-97 won't run until function is called on line 99
# print(b)
# foobar()
# print(b)
#Prediction: will print 500 500 300 500 

# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar() #this is where b value changes from 500 to 300
# print(b)
#Prediction: will print 500 500 300 300

# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
#Prediction: will print 1 3 2

# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
#Prediction: will print 1 3 5 10