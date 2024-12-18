import sympy as sp
import numpy as np
from sympy import symbols, Matrix
from scipy.optimize import fsolve


def simplify(matrix):
    return Matrix([x.simplify() for x in matrix])


def norm(matrix):
    sum = 0
    for x in matrix:
        sum += x**2
    return sp.sqrt(sum).simplify()


h, s, x, g, v = symbols('h s x g v')

# solve the inequality for x: h < s tan(x) - (g s^2) / (2 v^2 cos^2(x))
eq = s*sp.tan(x) - (g * s**2) / (2 * v**2 * sp.cos(x)**2) - h
solutions = sp.solve(eq, x, domain=sp.Interval(0, sp.pi/2))

def func(x):
    s = 100
    g = 9.82
    v = 80
    h = 15
    return s*np.tan(x) - (g * s**2) / (2 * v**2 * np.cos(x)**2) - h

solution1 = fsolve(func, 0.2)
solution2 = fsolve(func, 1.5)
