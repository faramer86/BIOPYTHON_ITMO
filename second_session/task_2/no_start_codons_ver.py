import Bio
import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Data import CodonTable
from Bio.Alphabet import IUPAC


def frame_check(seq):
    frame = []
    if len(seq) % 3 == 0:
        frame.extend(seq, seq[1:-2], seq[2:-1])
    elif len(seq) % 3 == 1:
        frame.extend((seq[1:], seq[:-1], seq[2:-2]))
    elif len(seq) % 3 == 2:
        frame.extend((seq[1:-1], seq[2:], seq[:2]))
    return frame


def proteins_from_dna(seq, table_type=1):
    import itertools as tl
    '''
    seq - DNA sequence
    table_type - type of codon table. Can be 1 (standard_table) or 2 (mito_table).
    '''
    frames_variants = frame_check(seq)
    result = list()
    for frame in frames_variants:
        stop_codons = [i for i in map(lambda x: frame.find(
            x), CodonTable.unambiguous_dna_by_id[table_type].stop_codons) if i != -1]
        for stop in stop_codons:
            pep_seq = frame[:stop + 3].translate(to_stop=True)
            if len(pep_seq) != 0 and pep_seq not in result:
                result.append((str(pep_seq)))
    return sorted(result, key=len)


if __name__ == "__main__":
    print(len('AGTACTAGAGCATTCTATGGAG') % 3)
    dna = Seq("AGTACTAGAGCATTCTATGGAG", generic_dna)
    print(proteins_from_dna(dna, 1))  # with standard_table
    print(proteins_from_dna(dna, 2))  # with mito_table
