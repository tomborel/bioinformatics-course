def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

def Reverse(Pattern):
    rev = ''
    for char in Pattern:
        rev = char + rev

    return rev


complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

def Complement(Pattern):
    comp = ''
    for char in Pattern:
        comp += complements.get(char)

    return comp


print(ReverseComplement('AAAACCCGGT'))