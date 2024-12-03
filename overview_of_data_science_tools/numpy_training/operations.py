'''
This script demonstrates basic operations with numpy ndarrays.

A complete list of universal functions (ufuncs) in numpy can be found here:
https://numpy.org/doc/stable/reference/ufuncs.html
'''

import numpy as np
import sys

if __name__ == '__main__':
    # Helper functions for creating arrays with specific data types
    create_range = lambda *args: np.arange(*args, dtype=np.int64)  # Tworzy tablicę liczb całkowitych / Creates an array of integers
    create_ones = lambda shape: np.ones(shape, dtype=np.int64)    # Tworzy tablicę z jedynkami / Creates an array filled with ones
    create_zeros = lambda shape: np.zeros(shape, dtype=np.int64)  # Tworzy tablicę z zerami / Creates an array filled with zeros

    # Arithmetic operations on arrays - element-wise
    print(create_range(0, 10) + create_ones([10]))  # Dodawanie / Addition
    print(create_range(0, 10) + 1)                 # Dodanie do każdego elementu wartości 1 / Adds 1 to each element
    print(create_range(0, 10, 2) * create_range(1, 11, 2))  # Mnożenie / Multiplication
    print(create_range(0, 10) ** 2)                # Potęgowanie / Squaring elements

    # Matrix operations
    a = np.array([[1, 0], [0, 1]])  # Macierz jednostkowa / Identity matrix
    b = np.array([[2, 2], [2, 2]])  # Macierz z wartościami 2 / Matrix with all elements as 2

    # Element-wise product
    print(a * b)  # Mnożenie elementów macierzy / Element-wise multiplication

    # Matrix multiplication (dot product)
    print(a.dot(b))  # Użycie dot() / Using dot()
    if sys.version_info >= (3, 5):
        print(a @ b)  # Użycie operatora @ / Using @ operator
        assert (a.dot(b) == a @ b).all()  # Porównanie wyników obu metod / Ensures both methods produce the same result

    # In-place operations
    a *= 2  # Mnożenie elementów przez 2 / Multiply elements by 2
    a += 1  # Dodawanie 1 do elementów / Add 1 to elements
    print(a)

    # Using ndarray methods
    c = np.arange(0, 9).reshape([3, 3])  # Tablica 3x3 z liczbami 0-8 / 3x3 array with numbers 0-8
    print(c.min())                       # Minimum element / Min value
    print(c.max(axis=1))                 # Maksimum w każdym wierszu / Max in each row
    print(c.cumsum(axis=1))              # Kumulatywna suma w wierszach / Cumulative sum across rows
    print(c.mean(axis=0))                # Średnia kolumn / Column-wise mean

    # Universal functions (ufuncs)
    angles = np.linspace(0, 7 / 4 * np.pi, 8)  # Równomierne rozłożenie wartości kątów / Evenly spaced angle values
    print(np.sin(angles) ** 2 + np.cos(angles) ** 2)  # Tożsamość trygonometryczna / Trigonometric identity
    print(np.sqrt(np.arange(1, 12, 2).cumsum()))  # Pierwiastek z kumulatywnej sumy liczb nieparzystych / Square root of cumulative sum of odd numbers
    print(np.floor(np.random.rand(10) * 2).astype(np.int8))  # Liczby losowe 0 lub 1 / Random integers 0 or 1
    print(np.sign(np.random.rand(10) - 0.5).astype(np.int8))  # Znak liczb losowych / Sign of random numbers
