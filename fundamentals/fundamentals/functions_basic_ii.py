#Countdown
def Countdown(number):
    list=[]
    for i in range(number, -1, -1):
        list.append(i)
    return list
print(Countdown(5))
#Print and Return
def Print_Return(list):
    print(list[0])
    return list[1]
print(Print_Return([1,2]))
#First Plus Length
def First_Plus_Length(list):
    sum=list[0]
    sum+=len(list)
    return sum
print(First_Plus_Length([1,2,3,4,5]))
#Values Greater than Second
def Values_Greater_than_Second(list):
    if len(list)<2:
        return False
    my_list=[]

    for i in range(0, len(list)):
        if list[i]> list[1]:
            my_list.append(list[i])
    print(len(my_list))
    return my_list
print(Values_Greater_than_Second([5,2,3,2,1,4]))



#This Length, That Value
def This_Length_That_Value(size, value):
    list=[]
    for i in range (size):
        list.append(value)
    return list
print(This_Length_That_Value(4,7))
print(This_Length_That_Value(5,10))
