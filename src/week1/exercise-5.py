def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(0, len(Genome)):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

print(PatternMatching('ATAT', 'GATATATGCATATACTT'))