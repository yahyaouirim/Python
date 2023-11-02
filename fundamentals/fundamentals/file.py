num1 = 42 #variable declaration, initialize numbers
num2 = 2.3 #variable declaration, initialize numbers
boolean = True #variable declaration, intialize boolean
string = 'Hello World' #variable declaration, intialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
#variable declaration, intialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
#variable declaration, intialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, intialize tuple
print(type(fruit)) #log statment, type check(tuple)
print(pizza_toppings[1]) #log statment, access value from list(sausage)
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) #log statment, access value from dictionary with name key(John)
person['name'] = 'George' #change value of name to george from list 
person['eye_color'] = 'blue' # add a key and value to list
print(fruit[2]) #log statment, third element of tuple(banana)

if num1 > 45: # if condition 42> 45 (false)
    print("It's greater") # log It's greater
else:   # else condition 42<= 45 (true)
    print("It's lower")  # log It's lower

if len(string) < 5: #if condition length string(11)< 5 (false)
    print("It's a short word!")# log It's a short word!
elif len(string) > 15: # else if condition length string 11> 15 (false)
    print("It's a long word!") # log It's a long word!
else:  # else condition lenght string 11<15 and 11>5 (true)
    print("Just right!") # # log Just right!

for x in range(5): # for loop x=0 to 4 
    print(x) # log x = 0 1 2 3 4
for x in range(2,5): #for loop x=2 to 4
    print(x) # log x=2 3 4
for x in range(2,10,3): #for loop x=2 to 10 x+3
    print(x) # log x= 2 5 8 
x = 0 # intialize x=0
while(x < 5): #while loop x=0< 5 
    print(x) # log x= 0 1 2 3 4
    x += 1

pizza_toppings.pop() # remove the last element from the list
pizza_toppings.pop(1) #remove the element with first index

print(person) # log person dictionary
person.pop('eye_color') # remove the eye_color element from  person dictionary
print(person) # log the person dictionary 

for topping in pizza_toppings: # for loop topping =pizza_toppings[0] to lenght.pizza_toppings
    if topping == 'Pepperoni': # if topping [0]==Pepperoni(true)
        continue # continue
    print('After 1st if statement') # log After 1st if statement 3 times
    if topping == 'Olives': # if condition topping[3]==Olives (true)
        break # exit

def print_hello_ten_times(): # declare a function print_hello_ten _times
    for num in range(10): # for loop num=0 to 9
        print('Hello') # log 10 times Hello

print_hello_ten_times() # call the function to log Hello 10 times

def print_hello_x_times(x): # declare a function print_hello_x _times
    for num in range(x): #for loop num=0 to x(paramater)
        print('Hello') # log Hello  x times Hello

print_hello_x_times(4) # call function print_hello_x _times to log 4 times Hello

def print_hello_x_or_ten_times(x = 10):# declare a function print_hello_x _times with initialize x=10 as a default
    for num in range(x): #for loop num=0 to x(10)
        print('Hello') # log Hello 10  times Hello

print_hello_x_or_ten_times()  # call function print_hello_x _times to log 10 times Hello
print_hello_x_or_ten_times(4)  # call function print_hello_x _times to log 4 times Hello


"""
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined

# num3 = 72
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment

# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7])  - IndexError: list index out of range


#print(boolean) - IndentationError: unexpected indent

# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'

# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'
