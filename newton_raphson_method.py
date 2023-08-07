"""
Coded by Frese
Ago 2023
"""
"""
Newton - Raphson: Find a root of the scalar-valued function func given a nearby scalar starting point x0. 
The Newton-Raphson method is used if the derivative fprime of func is provided, otherwise the secant method is used.
If the second order derivative fprime2 of func is also provided, then Halley’s method is used.
"""
import numpy as np

def newton_raphson(f, df, x0, error):
    # output is an estimation of the root of f 
    # recursive implementation
    if abs(f(x0)) < error:
        return x0
    else:
        return newton_raphson(f, df, x0 - f(x0)/df(x0), error)
    
#Example

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
estimate = newton_raphson(f, f_prime, 1.4, 1e-6)
print("estimate =", estimate) # Sehr gut!
print("sqrt(2) =", np.sqrt(2))
