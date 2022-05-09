def Count(Motifs):
    count = {}  # initializing the count dictionary

    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for key in count:
        for i in count:
            profile[key].append(count[key][i] / t)

    # insert your code here
    return profile


motifs = ['AACGTA',
          'CCCGTT',
          'CACCTT',
          'GGATTA',
          'TTCCGG']

print(Profile(motifs))
