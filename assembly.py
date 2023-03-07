def scorePatternList():
    return len()

def AvengersAssemble(I, E, Match, lmin, t=100):
    I_lens = [len(x) for x in I]

    P = None

    currIndices = I_lens
    exDict = get_excluded_dic(E, lmin)

    for i in range(t):

        currPatternList = []
        # While something
        while something:
            segments = chop(I, currIndices, lmin)
            # Search Segments for Patterns
            for seg in segments:
                # The order of things here will depend on Bhavya's implementation
                possPattern = Search(I, seg, Match, lmin)

                if len(possPattern) == 0:
                    #Do something
                    continue

                if possPattern is not None:
                    ppMedian = median_string(I, possPattern)
                    if is_excluded(ppMedian, ex_dic=exDict):
                        continue
                    else:
                        currPatternList.append(ppMedian)
                        #Possibly add to a library here as well?

                        #TODO Build New currIndex List

        # Score Pattern List, if better than Max than new best
        if scorePatternList(currPatternList) > scorePatternList(P):
            P = currPatternList

        # Alternatively, Store patterns to a library to be combined for the best possible pattern list
    if P is None:
        return "No Pattern List could be found."
    else:
        return P