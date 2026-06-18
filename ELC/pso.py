import numpy as np

def pso(f, N, S, a, b, b_hat, c, D):


    x = np.random.uniform(-S, S, size=(N, D))
    print("x is initially",x)
    v = np.random.normal(size=(N, D))
    p = x.copy()
    p_hat = x[np.argmin(np.apply_along_axis(f, 1, x))]

    for i in range(1000):
        r, r_hat = np.random.uniform(0, 1, (2, N, D))

        v = a * v + b * r * (p - x) + b_hat * r_hat * (p_hat - x)
        x = x + c * v
        print()
        print("x is in iteration ",i,x)
        print()

        for i in range(N):
            if f(x[i]) < f(p[i]):
                p[i] = x[i]
            if f(p[i]) < f(p_hat):
                p_hat = p[i]

    return p_hat

D = 2       # dimensions
N = 30      # particles
S = 10      # search space [-10,10]

a = 0.7     # inertia
b = 1.5     # cognitive coefficient
b_hat = 1.5 # social coefficient

c = 0.1     # step size

def f(x):
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

print(pso(f, N, S, a, b, b_hat, c, D))
