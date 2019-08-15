#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")


# function that takes arguments
def func(arg1,arg2):
    print(arg1, "  ", arg2)

# function that returns a value
def cube(x):
    return x*x*x


# function with default value for an argument
def power(num,x=1)
    result = 1
    for i in range(x):
        result = result * number
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# explore the output
func1()
print(func1()) #no return value. python evaluates it to be the python constant of none.  so just print the string represtation of that
print(func1) #not executing at all, because there is no (). so just print out the value of t he function itself

func2(10,20)
print(func2(10,20))
print(cube(3))

print(power(2)) #will default to 1
print(power(2,3)) #will use the number 3
print(power(x=3, num=2)) #if I supply the name along with the value, then there is no need to follow the order

print(multi_add(2,3,4,5)) #variable arg list always has to be the last parameters
