
"""
Change the value 10 in x to 15. 
Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
"""
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Update Values in Dictionaries and Lists

#Change the value 10 in x to 15. 
x[1][0]=15
print(x)
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']="Bryant"
print(students)
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)
#Change the value 20 in z to 30
z[0]['y']=30
print(z)
#2-Iterate Through a List of Dictionaries
students1 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for i in range(0, len(list)):
        output=""
        for k,v in list[i].items():
            output+= f"{k} - {v}, "
        print(output)
iterateDictionary(students1)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#3-Get Values From a List of Dictionaries
def iterateDictionary(key_name, some_list):
    for i in range(0, len(some_list)):
        for k, v in some_list[i].items():
            if k == key_name:
                print(v)
print("*****First name**********")
iterateDictionary('first_name', students1)
print("***********last name*********")

iterateDictionary('last_name', students1)
#4-Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for k,v in dict.items():
        print(len(v),k)
        for i in range(0,len(v)):
            print(v[i])
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


