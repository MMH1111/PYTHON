# #1. Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] #outside brackets tells me it's a list, inside brackets are also lists. It's a list of lists right now

# #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# def updateValue(arr):
#     arr[1][0] = 15
#     return arr
# print(updateValue(x))

# #1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
# students = [ #students is a list of dictionaries
#      {'first_name':  'Michael', 'last_name' : 'Jordan'}, #dictionaries have key value pairs
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# def updateNames(arr):
#     arr[0]['last_name'] = "Bryant"
#     return arr
# print(updateNames(students))

# #1.3. In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = { #sports_directory is one big dictionary
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# def updateDirectory(dict):
#     dict['soccer'][0] = "Andres"
#     return dict
# print(updateDirectory(sports_directory))

# #1.4. Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ] #z is a list of one dictionary

# def changeValue(list):
#     list[0]['y'] = 30
#     return list
# print(changeValue(z))


#2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key 
# and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    return some_list
print(iterateDictionary(students))

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for dict in some_list:
        for key in dict:
            print(key, dict[key])
iterateDictionary(students)
 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
def iterateDictionary2(key_name, some_list):
    first_name - Michael, last_name - Jordan
    first_name - John, last_name - Rosales
    first_name - Mark, last_name - Guillen
    first_name - KB, last_name - Tonel
    for dict in some_list:
        print(dict[key_name])

#3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints 
# the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
iterateDictionary2('first_name', students)
print(s["first_name"])

iterateDictionary2('last_name', students)

#4. Iterate Through a Dictionary with List Values
def printInfo(some_dict)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def iterateDictionary(some_list):
    return some_list
print(iterateDictionary(students))

def iterateDictionary(some_list):
    return some_list
print(iterateDictionary(students))

printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

