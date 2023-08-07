"""
Coded by Frese
Ago 2023
"""

"""
The Secant method is an approximation of the Newton-Raphson method. 
Instead of using the current value of x to figure out the next value of x,
we use the current and previous value of x to figure out the next value of x.
We use the Secant Method when the function's derivative is difficult to obtain.
"""

def secant(f, x1, x2, error):
    i=0
    xm1 = 0
    xm2 = 0
    check = 0
    if(f(x1) * f(x2) < 0):
        while(1):
            xm1 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
            check = f(x1) * f(xm1)
            if(check == 0):
                break
            
            x1 = x2
            x2 = xm1
            
            i = i + 1
            
            xm2 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
            if(abs(xm2 - xm1) < error):
                break
            
        return xm1
    else:
        return -1
    
# Example 

def f(x):
    return x**2 - 2

print(secant(f, 0, 2, 0.00001)) #output: 1.41421143847487 -> prima!