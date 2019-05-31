from itertools import combinations

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


def give_prefix(inp, total):
    inp = sorted(inp)
    inp = inp[:len(inp) / 2]
    return inp


def give_combinations(prefix):
    return list(combinations(prefix, 2))


def give_dif(combinations):
    dif = list()
    for pair in combinations:
        number = abs(pair[1] - pair[0])
        prefix = int(number)
        sufix = str(number - prefix)[1:4]
        num = float("{}{}".format(prefix, sufix))
        dif.append(num)
    print(dif)
    return dif


def give_order(prefix):
    ord = [i for i in range(1, len(prefix) + 1)]
    return list(combinations(ord, 2))


def give_possible_prot(dif, spectr):
    return list(filter(lambda x: x if x in spectr.keys() else None, dif))


def give_possible_order(ord, dif, prot):
    for p in prot:
        print(ord[dif.index(p)])


# Example:
total = 1988.21104821
p1 = 610.391039105
p2 = 738.485999105
p3 = 766.492149105
p4 = 863.544909105
p5 = 867.528589105
p6 = 992.587499105
p7 = 995.623549105
p8 = 1120.6824591
p9 = 1124.6661391
p10 = 1221.7188991
p11 = 1249.7250491
p12 = 1377.8200091

input = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

combination = give_combinations(give_prefix(input, total))
dif = give_dif(combination)
ord = give_order(give_prefix(input, total))
prot = give_possible_prot(dif, spectr)

print(give_possible_order(ord, dif, prot))
