def main(n, a, x):
    rez = 0
    for c in range(1, a + 1):
        for i in range(1, n + 1):
            rez += pow(34 * i + 73 * x ** 3 + 50 * c ** 2, 7) - 65 * i ** 6
    return rez


print(main(3, 2, 0.17))
