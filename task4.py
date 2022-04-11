from math import cos


def main(n):
    if n == 0:
        return 0.23
    if n >= 1:
        return pow(cos(main(n - 1) ** 2 - main(n - 1)), 3) + 1


print(main(8))
