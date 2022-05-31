def delete_duplicate_columns(table):
    new_list = []
    i = 0
    while table[0][i] not in new_list:
        new_list.append(table[0][i])
        i += 1

    for column in range(len(table)):
        del table[column][i]

    return table


def delete_empty_columns(table):
    for row in table:
        row.remove(None)
    return table


def delete_duplicate_rows(table):
    new_table = []
    for row in table:
        if row not in new_table:
            new_table.append(row)
    return new_table


def transformer(i, value):
    if i == 0:
        return f'{float(value):.3f}'
    if i == 1:
        return f'{value[2:5]} {value[5:8]}-{value[8:12]}'
    if i == 2:
        return "Нет" if value == "нет" else "Да"
    if i == 3:
        return f'{value[8:]}.{value[5:7]}.{value[2:4]}'


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(j, table[i][j])
    return table


def main(table):
    return transform(
        delete_duplicate_columns(
            delete_duplicate_rows(
                delete_empty_columns(table)
            )
        )
    )


print(main([['0.7', None, '0.7', '+77363938091', 'нет', '2004.08.09'],
            ['0.7', None, '0.7', '+77363938091', 'нет', '2004.08.09'],
            ['0.9', None, '0.9', '+72029545547', 'да', '2000.07.22'],
            ['0.7', None, '0.7', '+74259268543', 'нет', '2002.09.01']]))
