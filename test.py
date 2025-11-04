from sympy import symbols, diff
import random
x = symbols('x')
a = 2
while True:
    a = random.uniform(a, b)
    f = a**x
    f_prime = diff(f, x)
    log_part = str(f_p)