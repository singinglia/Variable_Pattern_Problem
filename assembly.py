from DouglasFunctions import *
from Search import Search


def scorePatternList(patternList):
    return len(patternList)

def adjustIndexes(currIdxes, augment = None, shift = None):
    newIdxs = []
    if augment is not None:
        for idx in currIdxes:
            newIdxs.append((idx[0]+1, idx[1]))

    elif shift is not None:
        for i, idx in enumerate(currIdxes):
            newIdxs.append((shift[1], idx[1]))

    return newIdxs

def AvengersAssemble(I, E, Match, lmin, jump=1, t=100):
    FAIL_MAX = 100
    I_lens = [len(x) for x in I]

    P = None

    currIndices = I_lens
    exDict = get_excluded_dic(E, lmin)

    for i in range(t):

        currPatternList = []
        # While something
        failCount = 0
        while True:

            try:
                segments = chop(I, currIndices, lmin)
            except:
                break

            # The order of things here will depend on Bhavya's implementation
            possPattern = Search(I, segments, Match, lmin)

            if len(possPattern) == 0:
                failCount += 1
                if failCount >= FAIL_MAX:
                    break
                else:
                    currIndices = adjustIndexes(currIndices, augment=jump)
                    continue

            if possPattern is not None:
                ppMedian = median_string(I, possPattern)
                if is_excluded(ppMedian, ex_dic=exDict):
                    continue
                else:
                    # Possibly add to a library here as well?
                    currPatternList.append(ppMedian)
                    currIndices = adjustIndexes(currIndices, shift=possPattern)

        # Score Pattern List, if better than Max than new best
        if scorePatternList(currPatternList) > scorePatternList(P):
            P = currPatternList

        # Alternatively, Store patterns to a library to be combined for the best possible pattern list
    if P is None:
        return "No Pattern List could be found."
    else:
        return P