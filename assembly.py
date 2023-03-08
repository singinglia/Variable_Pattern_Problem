from helper_functions import *
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
            newIdxs.append((shift[i][1], idx[1]))

    return newIdxs

def AvengersAssemble(I, E, Match, lmin, jump=1, t=100):
    FAIL_MAX = 100
    I_lens = [(0,len(x)) for x in I]

    P = []


    exDict = get_excluded_dic(E, lmin)

    for i in range(t):
        currIndices = I_lens
        currPatternList = []
        patternIdxes = []
        # While something
        failCount = 0
        while True:

            try:
                segments = chop(I, currIndices, lmin)
            except:
                break

            # The order of things here will depend on Bhavya's implementation
            # print(segments)
            possPattern = Search(I, segments, Match, lmin)
            # print("Poss Pattern")
            # print(possPattern)

            if len(possPattern) == 0:
                failCount += 1
                if failCount >= FAIL_MAX:
                    break
                else:
                    currIndices = adjustIndexes(currIndices, augment=jump)
                    continue

            if possPattern is not None:
                ppMedian = median_string(I, possPattern)
                if is_excluded(ppMedian, lmin, E, ex_dic=exDict):
                    continue
                else:
                    # Possibly add to a library here as well?
                    currPatternList.append(ppMedian)
                    patternIdxes.append(possPattern)
                    currIndices = adjustIndexes(currIndices, shift=possPattern)
        # print(i)
        # print("Canidate List")
        # print(currPatternList)

        # Score Pattern List, if better than Max than new best
        if scorePatternList(currPatternList) > scorePatternList(P):
            P = currPatternList
            bestIdxes = patternIdxes

        # Alternatively, Store patterns to a library to be combined for the best possible pattern list
    return P, bestIdxes