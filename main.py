# Create a class Reactangle wit the following attributes and methods:
# Attributes:  length, width
# Methods: area(), perimeter(), and display
# Create two instances of the class and call the methods for each instance.
# Display area and perimeter along with length and width  

class Rectangle:
  def dimensions(self):
    self.length= int(input())
    self.width= int(input())

  def Area(self):
    self.area=self.length*self.width
  
  def Perimeter(self):
    self.perimeter=2*(self.length+self.width)
  
  def display(self):
    print("Length:-",self.length,"\tBreadth:-",self.width)
    print("Area:-",self.area)
    print("Perimeter:-",self.perimeter)

f1=Rectangle()
f1.dimensions()
f1.Area()
f1.Perimeter()
f1.display()

f2=Rectangle()
f2.dimensions()
f2.Area()
f2.Perimeter()
f2.display()