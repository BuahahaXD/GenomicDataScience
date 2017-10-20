def PatternCount(Text, Pattern):
    count= 0
    i = 0
    while i <= len(Text) - len(Pattern):
        if Text[i: len(Pattern) + i] == Pattern:
                count += 1        
        i += 1
    return count

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = []
    for i in range(0, len(Text) - k):        
        Pattern = Text[i: k+i]
        Count.append(PatternCount(Text, Pattern))
    for i in range(0, len(Text) - k):
        if Count[i] == max(Count):
            FrequentPatterns.append(Text[i:k+i])
            
    return list(set(FrequentPatterns))

def ReverseComplement(Pattern):
    Pattern = str.replace(Pattern, 'C', 'X')
    Pattern = str.replace(Pattern, 'G', 'Y')
    Pattern = str.replace(Pattern, 'X', 'G')
    Pattern = str.replace(Pattern, 'Y', 'C')

    Pattern = str.replace(Pattern, 'T', 'X')
    Pattern = str.replace(Pattern, 'A', 'Y')
    Pattern = str.replace(Pattern, 'X', 'A')
    Pattern = str.replace(Pattern, 'Y', 'T')    

    return Pattern[::-1]

def PatternMatching(Pattern, Genome):
    occurrences = []
    for i in range(0, len(Genome)):
        if Genome[i: len(Pattern) + i] == Pattern:
            occurrences.append(i)
            i += len(Pattern)
    return occurrences
