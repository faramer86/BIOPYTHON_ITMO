spectr = {
    71.03: 'A',
    103.0: 'C',
    115.02: 'D',
    129.04: 'E',
    147.06: 'F',
    57.02: 'G',
    137.05: 'H',
    113.08: 'I',
    128.09: 'K',
    113.08: 'L',
    131.04: 'M',
    114.04: 'N',
    97.05: 'P',
    128.05: 'Q',
    156.10: 'R',
    87.03: 'S',
    101.04: 'T',
    99.06: 'V',
    186.07: 'W',
    163.06: 'Y',
}


def give_dif(list_1, list_2):
    result = list()
    for i, j in zip(list_1, list_2):
        number = abs(i - j)
        prefix = int(number)
        sufix = str(number - prefix)[1:4]
        num = float("{}{}".format(prefix, sufix))
        result.append(num)
    return result


def give_seq(prefix, spectr):
    prefix = sorted(prefix)
    prefix_2 = prefix[1:]
    dif = give_dif(prefix, prefix_2)
    seq = ''.join(list(map(lambda x: spectr[x], dif)))
    return seq


if __name__ == "__main__":

    # Example:
    p1 = 3524.8542
    p2 = 3710.9335
    p3 = 3841.974
    p4 = 3970.0326
    p5 = 4057.0646

    prefix = [p1, p2, p3, p4, p5]

    print(give_seq(prefix, spectr))
