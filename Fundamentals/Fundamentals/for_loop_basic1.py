# print("-" * 25)

# # 1. Basic 
# for i in range(0, 151): #For loop. In parentheses, the first is the starting number (inclusive), the 2nd is the ending one exclusive, the 3rd specifies the count
#     print(i)

# print("-" * 25)

# # 2. Multiples of Five
# for i in range(5, 1001, 5):
#     print(i)

# print("-" * 25)

# 3. Counting, the Dojo Way - NEED TO REVISE
# Print integers 1 to 100. 
# - If divisible by 5, print "Coding" instead. 
# - If divisible by 10, print "Coding Dojo".
# for i in range(1, 101):
#     if i % 10 == 0:
#         print("Coding Dojo")
#     elif i % 5 == 0:
#         print("Coding")
#     else: 
#         print(i)

# print("-" * 25)

# 4. Whoa. That Sucker's Huge
# Add odd integers from 0 to 500,000, and print the final sum.

# print("-" * 25)

# sum = 0

# for i in range(0, 500001):
#     if i % 2 == 1: #means it's an odd number, since it has a remainder of 1.
#         sum += i
# print(sum)

# 5. Countdown by Fours
# Print positive numbers starting at 2018, counting down by fours.
# y = 2018
# while y > 0:
#     print(y)
#     y = y - 4

# print("-" * 25)

# 6. Flexible Counter
# Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

# lowNum = 2
# highNum = 9
# mult = 3

# for i in range(lowNum, highNum + 1): #range(2, 10) or 2-10
#     if i % mult == 0: #if i is divisible by 3
#         print(i)

# print("-" * 25)