
from BWTSearch import BWTSearch


def scorePatternList(patternList):
    return len(patternList)

def concatInclusion(inList):
    start = 0
    text = ""
    startPos = []
    for i in inList:
        startPos.append(start)
        start += len(i)
        text = text + i
    return text, startPos

def buildSearchList(firstString, lmin, exclusionMap, E):
    searchList = []
    for i in range(len(firstString-lmin+1)):
        kmer = firstString[i:i+lmin]
        if is_excluded(kmer, lmin, E, ex_dic=exclusionMap):
            searchList.append(kmer)
    return searchList

def AvengersAssemble(I, E, Match, lmin):
    P = []

    ccI, posI = concatInclusion(I)

    bwtI = BWT(ccI)

    exDict = get_excluded_dic(E, lmin)

    searchList = buildSearchList(I[0], lmin, exDict, E)
    possPattern = BWTSearch(searchList, bwtI, posI, Match, lmin)


    return possPattern