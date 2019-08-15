#
# Example file for working with classes
#

class myClass():
  def method1(self): #the 1st argument to any of the methods of a class, is the self argument that refers to the object itself
    print ("myClass method1")
    
  def method2(self, someString):
    print ("myClass method2: " + someString)
    
class anotherClass(myClass): #anotherClass inherits from myclass
  def method2(self):
    print ("anotherClass method2")
    
  def method1(self):
    myClass.method1(self); #call the inherited method on the superclas
    print ("anotherClass method1")
      
def main():
  c = myClass() #no need to supply the self keyword when calling the class methods
  c.method1()
  c.method2("This is a string")
  c2 = anotherClass() #c2 is an instance of another class
  c2.method1()
  
if __name__ == "__main__":
  main()
