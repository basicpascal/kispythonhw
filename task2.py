from math import ceil, cos


def main(y):
    if y < 187:
        return pow(64 * y ** 3, 6)
    if y >= 235:
        return 9 * cos(y) ** 6 - 60 * ceil(33 * y ** 2 - 1 - y)
    else:
        return cos(y) - 8 * pow(y ** 3 / 53 + y ** 2 + 53, 7)


print(main(233))