
from BWTSearch import BWTSearch
from DouglasFunctions import *


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
    lmin = int(lmin)
    for i in range(len(firstString)-lmin+1):
        kmer = firstString[i:i+lmin]
        if not is_excluded(kmer, lmin, E, ex_dic=exclusionMap):
            searchList.append(kmer)
    return searchList

def toIndexLists(patternList, posI):
    allPatternIndexes = []
    foundPatterns = []
    for patternLocs in patternList:
        pattern = patternLocs[-1]
        idxList = []
        for i, stringStart in enumerate(posI):
            start = patternLocs[i] - stringStart
            idxList.append((start, start+ len(pattern)))
        allPatternIndexes.append(idxList)
        foundPatterns.append(pattern)

    return foundPatterns, allPatternIndexes


def YoungAvengersAssemble(I, E, Match, lmin):
    P = []

    ccI, posI = concatInclusion(I)

    exDict = get_excluded_dic(E, lmin)

    searchList = buildSearchList(I[0], lmin, exDict, E)
    possPatternMap = BWTSearch(searchList, ccI, posI, Match, lmin)
    bestPatternList = get_pattern_list(posI, possPatternMap)

    patterns, idxes = toIndexLists(bestPatternList, posI)

    return patterns, idxes