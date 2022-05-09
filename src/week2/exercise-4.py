def SkewArray(Genome):
    arr = [0]
    for i in range(0, len(Genome)):
        if Genome[i] == 'A' or Genome[i] == 'T':
            arr.append(arr[i])
        elif Genome[i] == 'C':
            arr.append(arr[i] - 1)
        else:
            arr.append(arr[i] + 1)
    return arr

def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)
    m = min(skew)
    for i in range(0, len(skew)):
        if skew[i] == m:
            positions.append(i)
    return positions

print(MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))
