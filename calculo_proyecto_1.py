#!/usr/bin/env python3
"""
EJERCICIO 1: Implemente en lenguaje Python una función que aproxime mediante un Polinomio de Taylor de tercer orden centrado en x=1 para predecir f(2), siendo f(x) = 25x**3 – 6x**2 + 7x – 88. Calcule luego el error relativo de la aproximación.

EJERCICIO 2: Implemente en lenguaje Python el método de Newton-Raphson para aproximar la solución de f(x) = 0, siendo f(x) = exp(-x)-ln(x).

Escriba aqui los nombres de los integrantes del grupo:
- Elder Gomes.
"""
import math

# Error relativo
def eR(vreal, vaprox):
	return abs(vreal - vaprox) / vreal

# Derivada numerica de la funcion
def diff(f, h = 0.01):
	return lambda x : (f(x + h) - f(x)) / h

# Polinomio de Taylor
def pTaylor(f, n, x0, x):
	aprox = 0
	for i in range(n):
		if i == 0:
			aprox = f(x0)
			fPrime = f
		else:
			fPrime = diff(fPrime)
			aprox += fPrime(x0) * (x-x0)**i / math.factorial(i)

	vReal = f(x)
	print("Aproximacion:", aprox)
	print("Error relativo:", eR(vReal, aprox))
		
# Metodo Newton-Raphson
def nRaphson(f, xn, es):
	ea = 100
	i = 1
	mp = 0
	fPrime =  diff(f)
	while (ea > es):
		mp = xn
		xn = xn - f(xn) / fPrime(xn)
		if i > 1:
			ea = eR(xn, mp)*100

		i = i + 1
	print("Iteracion:", i)
	print("Aproximacion:", xn)

if __name__ == '__main__':
	print("EJERCICIO 1: P3=25x**3 – 6x**2 + 7x – 88, x0=1, x=2")
	f1 = lambda x:25*(x**3)-6*(x**2)+7*x-88
	pTaylor(f1, 3, 1, 2)

	print()

	print("EJERCICIO 2: f(x)=exp(-x)-ln(x)")
	f2 = lambda x : math.exp(-x) - math.log(x)
	nRaphson(f2, 0.5, 1)
