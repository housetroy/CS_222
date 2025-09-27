def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Has to be a number")
    return (fahrenheit - 32) * 5.0 / 9.0

def fibonaci(n):
    if not isinstance(n, int):
        raise TypeError("Munt be an integer")
    if n < 0:
        raise ValueError("must be a non-negative integer")
    
    if n == 0 or n == 1:
        return n
    
    x, y = 0, 1

    for i in range(2, n +1):
        x, y = y, x + y
    return y