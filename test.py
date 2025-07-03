from sympy import symbols, integrate , exp, cos, atan
x, t = symbols('x,t')
print('hello')
inte=integrate((t**2),(t,0,x))
print(inte)
inte2=integrate(exp(t-cos(t))/(1+t**2),(t,0,x*atan(x)))
print(inte2)