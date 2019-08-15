# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# # re-declaring the variable works
f="abc"
print(f)

# # ERROR: variables of different types cannot be combined
print("this is string" + str(123))
#print("this is string" + 123) will work in JavaScript

# Global vs. local variables in functions
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

del f #undefine varibles in real time by using the del statement
print(f)
#i need to tell the functions that f is global