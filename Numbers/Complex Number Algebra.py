"""
Show addition, multiplication, negation, and inversion of complex numbers in separate functions.
(Subtraction and division operations can be made with pairs of these operations.)
Print the results for each operation tested.
a+j*b
"""
from math import sqrt


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f'{self.a: 1.2f}+j*{self.b: 1.2f}')

    def negate(self):
        return ComplexNumber(-self.a, - self.b)

    def modulus(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def invert(self):
        a_inv = self.a / (self.a ** 2 + self.b ** 2)
        b_inv = - self.b / (self.a ** 2 + self.b ** 2)
        return ComplexNumber(a_inv, b_inv)


def add_complex(x, y):
    return ComplexNumber(x.a + y.a, x.b + y.b).show()


def subtract_complex(x, y):
    return ComplexNumber(x.a - y.a, x.b - y.b).show()


def multiply_complex(x, y):
    return ComplexNumber(x.a * y.a - x.b * y.b, x.a * y.b + x.b * y.a).show()


def divide_complex(x, y):
    a_new = (x.a * y.a + x.b * y.b) / (y.a ** 2 + y.b ** 2)
    b_new = (x.b * y.a - x.a * y.b) / (y.a ** 2 + y.b ** 2)
    return ComplexNumber(a_new, b_new).show()


n1 = ComplexNumber(3, 2)
n2 = ComplexNumber(1, 1)

print('n1 = ')
n1.show()
print('n2 = ')
n2.show()

print('n1 inverted = ')
n1.invert().show()
print('n1 negated = ')
n1.negate().show()
print(f'n1 modulus = {n1.modulus(): 1.2f}')

print('n1+n2 =')
add_complex(n1, n2)

print('n1-n2 =')
subtract_complex(n1, n2)

print('n1*n2 = ')
multiply_complex(n1, n2)

print('n1/n2 = ')
divide_complex(n1, n2)
