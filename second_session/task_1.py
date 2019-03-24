from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Data import CodonTable

dna = Seq("AGTACTAGAGCATTCTATGGAG", generic_dna)


def proteins_from_dna(seq, table_type=2):
    import itertools as tl
    '''
    seq - DNA sequence
    table_type - type of codon table. Can be 1 (standard_table) or 2 (mito_table).
    '''
    stop_codons = [i for i in map(lambda x: seq.find(
        x), CodonTable.unambiguous_dna_by_id[table_type].start_codons) if i != -1]
    start_codons = [i for i in map(lambda x: seq.find(
        x), CodonTable.unambiguous_dna_by_id[table_type].stop_codons) if i != -1]
    result = list()
    for pair in list(tl.product(start_codons, stop_codons)):
        result.append((seq[pair[0]:pair[1] + 3].translate())[::-1])
    return sorted(result)


print(proteins_from_dna(dna, 1))
print(proteins_from_dna(dna, 2))
