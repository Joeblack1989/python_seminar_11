# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

import math
from sympy.plotting import plot
from sympy import Symbol, solve, diff

# import matplotlib as mpl

x = Symbol('x')
fx = (-12 * x ** 2 + 10 * x - 30)
print('Дана функция: -12 * x ** 2 + 10 * x - 30')
print('Необходимо:')
print()
print('1. Определить корни')
print(solve(fx))
print()
print('2. Найти интервалы, на которых функция возрастает')
print(solve(diff(fx) > 0))
print()
print('3. Найти интервалы, на которых функция убывает')
print(solve(diff(fx) < 0))
print()
print('4. Построить график')
plot(fx)
print()
print('5. Вычислить вершину')
x_top = solve((diff(fx)))[0]
y_top = -12 * x_top ** 2 + 10 * x_top - 30
print(f'({x_top}: {y_top})')
print('6. Определить промежутки, на котором f > 0')
if solve(fx > 0):
     print(solve(fx > 0))
else:
    print('Функция полностью лежит ниже оси у')
print()
print('7. Определить промежутки, на котором f < 0')
if solve(fx < 0):
     print(solve(fx < 0))
else:
    print('Функция полностью лежит выше оси у')
print()