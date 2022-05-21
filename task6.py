def zero(items, left, right):
    if items[0] == 1986:
        return left
    if items[0] == 2019:
        return right


def four(items, left, middle, right):
    if items[4] == 1998:
        return left
    if items[4] == 2012:
        return middle
    if items[4] == 1976:
        return right


def two(items, left, middle, right):
    if items[2] == 2013:
        return left
    if items[2] == 1961:
        return middle
    if items[2] == 1960:
        return right


def three(items, left, middle, right):
    if items[3] == 1984:
        return left
    if items[3] == 1993:
        return middle
    if items[3] == 1988:
        return right


def one(items, left, middle, right):
    if items[1] == 'VCL':
        return left
    if items[1] == 'VHDL':
        return middle
    if items[1] == 'MINID':
        return right


def main(items):
    return three(
        items,
        one(
            items,
            two(
                items,
                3,
                4,
                four(items, 0, 1, 2)
            ),
            four(items, 8, zero(items, 9, 10), two(items, 5, 6, 7)),
            11
        ),
        12,
        13
    )


print(main([1986, 'VHDL', 2013, 1993, 1998]))
