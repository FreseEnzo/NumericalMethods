"""
Coded by Frese
Ago 2023
"""

"""
The False Position Method: It's an algorithm that uses the value of the previous 
estimate to estimate a value that's closer to the actual value.
The false position method does this over multiple iterations and 
keeps the root of the function bracketed. Similar to Bisection Method
"""
import numpy as np

def false_position(f, a, b, error): 
    # approximates a root, R, of f bounded 
    # by a and b to within error 
    # | f(w) | < error with w the weighted average
    # between a and b Recursive implementation

    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    w = (a*abs(f(a)) + b*abs(f(b))) / (abs(f(a)) + abs(f(b))) # weighted average (here is the unique difference between bisection and false position)
    
    if np.abs(f(w)) < error:
        # stopping condition, report w as root
        return w
    elif np.sign(f(a)) == np.sign(f(w)):
        # case where w is an improvement on a. 
        # Make recursive call with a = m
        return false_position(f, w, b, error)
    elif np.sign(f(b)) == np.sign(f(w)):
        # case where w is an improvement on b. 
        # Make recursive call with b = w
        return false_position(f, a, w, error)


# Example

"""
# 1 - The sqrt(2) can be computed as the root of the function f(x)=x^2-2 . Starting at a=0
 and b=2, use my_bisection to approximate the sqrt(2) to a tolerance of |f(x)|<0.1 and |f(x)|<0.01.
 Verify that the results are close to a root by plugging the root back into the function.
"""

f = lambda x: x**2 - 2 # A lambda function is a small anonymous function.
error = [0.1, 0.01]
a = 0
b = 2
r1 = false_position(f,a,b,error[0]) 
r2 = false_position(f,a,b,error[1])
print(r1, r2) # output:1.4380740283626157 1.4141274320340094 -> thats not so good as bisection method
print(f(r1), f(r2)) # output: 0.06805691105108114 -0.000243605968898164
