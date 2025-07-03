import sympy
x, t = sympy.symbols('x,t')
print('hello')
inte=sympy.integrate((t**2),(t,0,x))
print(inte)
inte2=sympy.integrate(sympy.exp(t-sympy.cos(t))/(1+t**2023),(t,0,x*sympy.atan(x)))
print(inte2)