import re


def locate_active_site(fasta):
    '''
    return site and start index of IL
    '''
    with open(fasta) as file:
        string = file.read()
    pattern = 'K(K|R)CGH(L|M|Q|R)'
    match = re.search(pattern, string)
    return match.start(), match.group()
