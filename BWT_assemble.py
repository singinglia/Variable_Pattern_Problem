
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

def getTotalConcatPos(inList):
    start = 0
    startPos = []
    for i in inList:
        startPos.append(start)
        start += len(i)
    return startPos

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


def get_segments(pi, sstarts):
    insertion_points = [bisect.bisect_left(pi, x) for x in sstarts] + [len(pi)]

    return [pi[insertion_points[i]:insertion_points[i + 1]] for i in range(len(sstarts))]

def convertSegs(patternMap, start, partialPoss, totalPos):
    convertPosMap = {}
    #Get segment
    for pattern in patternMap:
        posList = []
        groups = get_segments(patternMap[pattern], partialPoss)
        for i, points in enumerate(groups):
            adjustor = start+totalPos[i]-partialPoss[i]
            posList.extend([x+adjustor for x in points])
        convertPosMap[pattern] = posList
        # finalGroups = get_segments(posList, totalPos)
    return convertPosMap


import math
def YoungAvengersAssemble(I, E, Match, lmin):
    iLen = len(I[0])
    iLenList = [len(x) for x in I]
    minLen = min(iLenList)
    print(minLen)
    SEG_LEN = 1000

    exDict = get_excluded_dic(E, lmin)


    if iLen > SEG_LEN:
        posI = getTotalConcatPos(I)
        possPatternMap = {}
        for i in range(math.ceil(iLen/SEG_LEN)*2):
            start = int(i*SEG_LEN/2)
            print(start)
            if start > minLen:
                break
            partialEnd = start+SEG_LEN
            if partialEnd >= iLen:
                partial = [x[start:] for x in I]
            else:
                partial = [x[start:partialEnd] for x in I]

            ccI, partialPoss = concatInclusion(partial)

            searchList = buildSearchList(partial[0], lmin, exDict, E)

            segMap = BWTSearch(searchList, ccI, partialPoss, Match, lmin)
            segMap = convertSegs(segMap, start, partialPoss, posI)
            # print("Map Length:", len(segMap))
            for key in segMap:
                if key in possPatternMap:
                    newList = list(set(possPatternMap[key] + segMap[key]))
                    newList.sort()
                    possPatternMap[key] = newList
                else:
                    possPatternMap[key] = segMap[key]
            # print("Total Map Length:", len(possPatternMap))


    else:
        ccI, posI = concatInclusion(I)
        searchList = buildSearchList(I[0], lmin, exDict, E)
        possPatternMap = BWTSearch(searchList, ccI, posI, Match, lmin)

    bestPatternList = get_pattern_list(posI, possPatternMap)
    patterns, idxes = toIndexLists(bestPatternList, posI)

    return patterns, idxes