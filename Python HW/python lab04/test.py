
# Importing the modules
from mathematics import whoami as math_whoami
from mathematics.numbers import whoami as numbers_whoami
from mathematics.numbers import series
from mathematics.numbers import simple
from mathematics.geometry import whoami as geometry_whoami
from mathematics.geometry import cube
from mathematics.geometry import circle
from mathematics.geometry import rectangle

# Testing the getname function from each whoami module
print("Testing mathematics.whoami:")
print(math_whoami.getname())  

print("\nTesting mathematics.numbers.whoami:")
print(numbers_whoami.getname())  

print("\nTesting mathematics.geometry.whoami:")
print(geometry_whoami.getname()) 

# Testing the series module
print("\nTesting mathematics.numbers.series:")
print(series.sum(list=[1,2,3])) 
print(series.average(list=[1,2,3]))  

# Testing the simple module
print("\nTesting mathematics.numbers.simple:")
print(simple.addition(left= 5, right= 3)) 
print(simple.subtraction(left=5,right= 3)) 
print(simple.multiplication(left=5,right=3))
print(simple.division(left=5,right=3))  

# Testing the geometry module
print("\nTesting mathematics.geometry.cube:")
print(cube.surface_area(side=3))  
print(cube.volume(side=3))  

print("\nTesting mathematics.geometry.circle:")
print(circle.circumference(radius=3)) 
print(circle.area(radius=3)) 

print("\nTesting mathematics.geometry.rectangle:")
print(rectangle.perimeter(length=3, width=4)) 
print(rectangle.area(length=3, width=4))  

