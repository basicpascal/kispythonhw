from math import ceil


def main(z, x):
    sum = 0
    n = len(x)
    for i in range(1, n+1):
        sum += 48 * x[ceil(i / 3)-1] ** 2 + 95 * z[n - ceil(i / 4)] + 0.03
    return sum


print(main([-0.97, 0.33], [-0.75, -0.64]))
