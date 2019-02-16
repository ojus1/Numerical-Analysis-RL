from Function import Function, Derivative
import math, random

# Function to find the sign of a number
def Sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class TranscendentalSolvers:
    def __init__(self):
        pass
    
    @staticmethod
    def NewtonRaphson(f):
        ''' Expression should be of the form: f(x) = 0 '''
        # Convergence threshold
        thres = 1e-3
        # initialization of x
        x = 1
        
        #Solving begins
        while abs(f(x)) > thres:
            x = x - f(x) / Derivative(f, x)
        return x
    
    @staticmethod
    def Bisection(f):
        ''' Expression should be of the form: f(x) = 0 '''
        # Convergence threshold
        thres = 1e-4
        # initialization of x
        xn_1 = random.randint(0, 10)
        i = 0
        xn = xn_1
        found = False
        while not found:
            if Sign(f(xn-i)) != Sign(f(xn)):
                xn = xn - i
                found = True
            elif Sign(f(xn+i)) != Sign(f(xn)):
                xn = xn + i
                found = True
            i += 1
        #Solving begins
        x = xn
        while abs(f(x)) > thres:
            #print(x)
            x = (xn_1 + xn) / 2
            if Sign(f(xn_1)) != Sign(f(x)):
                xn = x
            else:
                xn_1 = x
        return x

    @staticmethod
    def RegulaFalsi(f):
        ''' Expression should be of the form: f(x) = 0 '''
        # Convergence threshold
        thres = 1e-3
        # initialization of x
        xn_1 = random.randint(0, 10)
        i = 0
        xn = xn_1
        found = False
        while not found:
            if Sign(f(xn-i)) != Sign(f(xn)):
                xn = xn - i
                found = True
            elif Sign(f(xn+i)) != Sign(f(xn)):
                xn = xn + i
                found = True
            i += 1
        #Solving begins
        x = xn
        while abs(f(x)) > thres:
            #print(x)
            x = xn_1 - f(xn_1) * (xn - xn_1) / (f(xn) - f(xn_1))
            xn = x
        return x

    @staticmethod
    def Secant(f):
        ''' Expression should be of the form: f(x) = 0 '''
        # Convergence threshold
        thres = 1e-3
        # initialization of x
        xn_1 = random.randint(0, 10)
        i = 0
        xn = xn_1
        found = False
        while not found:
            if Sign(f(xn-i)) != Sign(f(xn)):
                xn = xn - i
                found = True
            elif Sign(f(xn+i)) != Sign(f(xn)):
                xn = xn + i
                found = True
            i += 1
        #Solving begins
        x = xn
        while abs(f(x)) > thres:
            #print(x)
            x = xn - f(xn) * (xn_1 - xn) / (f(xn_1) - f(xn))
            xn = x
        return x

if __name__ == "__main__":
    f1 = Function("1.3*x**3- 1.2")
    print(TranscendentalSolvers.NewtonRaphson(f1))
    print(TranscendentalSolvers.RegulaFalsi(f1))
    print(TranscendentalSolvers.Secant(f1))
    print(TranscendentalSolvers.Bisection(f1))