'''3. Create a function to add two numbers.
4. Create a function to subtract two numbers.
5. Create a function to multiply two numbers.
6. Create a function to divide two numbers.
7. Create a function to find the square of a number.
8. Create a function to find the cube of a number.

'''
def add(a, b):
    sum = a+b
    print("the addition of",a, "and",b,"is",sum)
    return sum

def sub(a, b):
    diffrence = a-b
    print("the sub of",a, "and",b,"is",diffrence)
    return diffrence

def multiply(a, b):
    product = a*b
    print("the product of",a, "and",b,"is",product)
    return product

def div(a, b):
    divisionn = a/b
    print("the division of",a, "and",b,"is",divisionn)
    return divisionn


def square(a):
    square = a**2
    print("the square of",a,"is",square)
    return square


def cube(a):
    cube = a**3
    print("the addition of",a,"is",cube)
    return cube





add(10, 12)
sub(10, 5)
multiply(20, 2)
div(10 , 5)
square(20)
cube(6)
