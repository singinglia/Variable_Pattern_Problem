from helpers import *
import bisect


def isInAllInclusion(pi, sstarts):
    pi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sstarts = [0, 4, 8, 100]

    if len(pi) < len(sstarts):
        return False

    insert_points = [bisect.bisect_left(pi, x) for x in sstarts]
    print(insert_points)
    if len(set(insert_points)) < len(insert_points):
        return False

    if max(insert_points) >= len(pi):
        return False

    return True


def BWTSearch(possPatterns, bwt, inclusionStarts, Match, lmin):

    d = int((1 -Match)*lmin)

    matchMap = getApproximatePatternLocations(bwt, possPatterns, d)

    validMatches = {}
    for pattern in matchMap:
        if isInAllInclusion(matchMap[pattern], inclusionStarts):
            validMatches[pattern] = matchMap[pattern]

    return
