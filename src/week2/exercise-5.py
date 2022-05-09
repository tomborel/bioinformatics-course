def HammingDistance(p, q):
    distance = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            distance = distance + 1
    return distance


def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here

    for i in range(0, len(Text) - len(Pattern) + 1):
        hamming = HammingDistance(Pattern, Text[i:i+len(Pattern)])
        if hamming <= d:
            positions.append(i)

    return positions

print(ApproximatePatternMatching(
'CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA',
    'AATCCTTTCA', 3))

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count = count+1
    return count

print(HammingDistance('TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC', 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'))