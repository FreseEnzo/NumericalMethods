"""
Coded by Frese
Ago 2023
"""

"""
Bissection Method: The bisection method is an approximation method 
to find the roots of the given equation by repeatedly dividing the interval.
"""
import numpy as np

def bisection(f, a, b, error): 
    # approximates a root, R, of f bounded 
    # by a and b to within error 
    # | f(m) | < error with m the midpoint 
    # between a and b Recursive implementation

    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # get midpoint
    m = (a + b)/2 #-> mid
    
    if np.abs(f(m)) < error:
        # stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return bisection(f, m, b, error)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return bisection(f, a, m, error)


# Example

"""
The sqrt(2) can be computed as the root of the function f(x)=x^2-2 . Starting at a=0
 and b=2, use my_bisection to approximate the sqrt(2) to a tolerance of |f(x)|<0.1 and |f(x)|<0.01.
 Verify that the results are close to a root by plugging the root back into the function.
"""

f = lambda x: x**2 - 2 # A lambda function is a small anonymous function.
error = [0.1, 0.01]
a = 0
b = 2
r1 = bisection(f,a,b,error[0]) 
r2 = bisection(f,a,b,error[1])
print(r1, r2) # output: 1.4375 1.4140625 -> thats really good
print(f(r1), f(r2)) # output: 0.06640625 -0.00042724609375
