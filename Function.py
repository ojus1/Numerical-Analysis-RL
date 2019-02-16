#supported basic functions
from math import *

class Function:
    ''' Expression should be of the variable x '''
    def __init__(self, func_string):
        self.func_string = func_string
    def __call__(self, x):
        return eval(self.func_string)

class MultivariateFunction:
    ''' Expression should be of the variables x, y, z & u '''
    def __init__(self, func_string):
        self.func_string = func_string
    
    def __call__(self, vars):
        x, y, z, u = vars
        return eval(self.func_string)


def Derivative(f, x):
    '''Used this for reference: https://en.wikipedia.org/wiki/Numerical_differentiation'''
    h =  1e-7
    f_prime = (f(x + h) - f(x)) / h
    return f_prime

if __name__ == "__main__":
    f1 = Function("sin(x)+3")
    f2 = MultivariateFunction("x + y")
    print(Derivative(f1, 5))
    print(f2([5, 3, 0, 0]))