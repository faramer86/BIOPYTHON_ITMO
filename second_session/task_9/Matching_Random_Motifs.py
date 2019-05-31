import random
from Bio.SeqUtils import GC


def give_prob(gc, seq, n):
    content = dict()
    content['G'], content['C'] = gc / 2, gc / 2
    content['A'], content['T'] = (1 - gc) / 2, (1 - gc) / 2
    # Count prob for this seq to be synthesized:
    value = reduce(lambda x, y: x * content[y], list(seq), 1.0)
    # 1 - this prob give us prob for this seq not to be synth-d
    # If we multiply it n times, we obtain prob of not obtaining this seq n times
    # If we substract this value from 1
    # we will get value for this seq to be synth-d at least once
    prob = round(1 - (1 - value)**n, 3)
    return prob


if __name__ == "__main__":

    # n = int(input())
    # GC_content = float(input())
    # seq = input()

    # Example:

    n = 90000
    GC_content = 0.6
    seq = 'ATAGCCGA'

    print(give_prob(GC_content, seq, n))
