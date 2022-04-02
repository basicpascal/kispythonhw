from math import *


def main(x, z):
    a = (x ** 5 / 84 - 67 * pow(z - 1, 4)) / (pow(z ** 2 + x ** 3 / 90, 2))
    b = (9 - 60 * pow(ceil(33 * z ** 2 - 1 - x), 7)) / \
        pow(33 * z ** 2 + 80 + 69 * x, 4)
    return a + sqrt(b)


print(main(0.87, 0.08))
