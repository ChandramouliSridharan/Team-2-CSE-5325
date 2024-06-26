def add(x, y):
    """Addition"""
    return x + y
 
def subtract(x, y):
    """Subtraction"""
    return x - y
 
def multiply(x, y):
    """Multiplication"""
    return x * y
 
def divide(x, y):
    """Division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def pow(x,y):
    """Power function"""
    return x ** y

def modulo(x, y):
    """Modulo Operation"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x % y
  
def sqrt(x):
    """Square function"""
    return x ** 0.5