from BWT_helpers import *
import bisect
from BWT import *

def isInAllInclusion(pi, sstarts):

    if len(pi) < len(sstarts):
        return False

    insert_points = [bisect.bisect_left(pi, x) for x in sstarts]
    # print(insert_points)
    if len(set(insert_points)) < len(insert_points):
        return False

    if max(insert_points) >= len(pi):
        return False

    return True


def BWTSearch(possPatterns, concatI, inclusionStarts, Match, lmin):

    bwtI = BWT(concatI)
    d = lmin - int((Match)*lmin) + 1
    d = int(d)
    # print("d", d)

    matchMap = getApproximatePatternLocations(bwtI, concatI, possPatterns, d)

    validMatches = {}
    for pattern in matchMap:
        # print(pattern, ": ", len(matchMap[pattern]))
        if isInAllInclusion(matchMap[pattern], inclusionStarts):
            validMatches[pattern] = matchMap[pattern]
    # print('Starts', inclusionStarts)
    return validMatches
