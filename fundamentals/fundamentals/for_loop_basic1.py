print("Basic - Print all integers from 0 to 150.")
for i in range(151):
    print(i)

print("**Multiples of Five - Print all the multiples of 5 from 5 to 1,000**")
for i in range(5, 1000):
    if i% 5 == 0:
        print(i)

print("Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print Coding instead. If divisible by 10, print Coding Dojo.")
for i in range(1, 100):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else : 
        print(i)

print("Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.")
sum=0
for i in range(500001):
    if i % 2 != 0:
        sum = sum + i 
        
print(sum)

print("Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.")
for i in range( 2018, 0, -4):
    print(i)

print("Flexible Counter")
lowNum=2
highNum= 9
mult=3
for i in range(lowNum, highNum+1, 1):
    if i % mult == 0:
        print(i)


        
