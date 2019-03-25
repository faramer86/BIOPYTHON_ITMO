import Bio
import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Data import CodonTable
from Bio.Alphabet import IUPAC
import re


def proteins_from_dna(seq, table_type=1):
    import itertools as tl
    '''
    seq - DNA sequence
    table_type - type of codon table. Can be 1 (standard_table) or 2 (mito_table).
    '''
    start_codons = [i for i in map(lambda x: seq.find(
        x), CodonTable.unambiguous_dna_by_id[table_type].start_codons) if i != -1]
    stop_codons = [i for i in map(lambda x: seq.find(
        x), CodonTable.unambiguous_dna_by_id[table_type].stop_codons) if i != -1]
    result = list()
    for pair in list(tl.product(start_codons, stop_codons)):
        pep_seq = str(seq[pair[0]:pair[1] + 3].translate(to_stop=True))
        if len(pep_seq) != 0 and pep_seq not in result:
            result.append((pep_seq))
    return sorted(result, key=len)


if __name__ == "__main__":
    dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",  generic_dna)
    print(proteins_from_dna(dna, 1))  # with standard_table
    print(proteins_from_dna(dna, 2))  # with mito_table
