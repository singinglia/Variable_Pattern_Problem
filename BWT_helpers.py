def isApproxMatch(pattern, possMatch, d):
    mmCount = 0
    for i, letter in enumerate(pattern):
        if letter != possMatch[i]:
            mmCount += 1
            if mmCount > d:
                return False
    return True

def getPatternSeeds(p, d):
    seedList = []
    k = int(len(p)/(d+1))
    for i in range(d+1):
        start = i*k
        if i == d:
            seedList.append((p[start:], start))
        else:
            seedList.append((p[start:start+k], start))
    return seedList


def getPatternStart(seedShift, foundIdx):
    start = foundIdx - seedShift
    if start < 0:
        return None
    return start


def writeMapFile(m, fileName):
    f = open(fileName, "w")
    for key in m:
        f.write(key + ":")
        for item in m[key]:
            f.write(" ")
            f.write(str(item))
        f.write("\n")
    # close file
    f.close()

def printMap(m):
    for key in m:
        print(key + ":", *m[key])

def BWMatchingRange(pattern, bwt):
    top = 0
    bottom = len(bwt.lastCol) - 1
    pL = [i for i in pattern]

    while top <= bottom:
        if len(pL) > 0:
            currLetter = pL.pop()
            # print(currLetter)
            # print(bwt.lastCol[top:bottom+1])
            if currLetter in bwt.lastCol[top:bottom+1]:
                firstOcc = bwt.firstSeen[currLetter]
                # print("first occ", firstOcc)
                top = firstOcc + bwt.CountSymbol(top, currLetter)
                bottom = firstOcc + bwt.CountSymbol(bottom + 1, currLetter) -1
                # print(top, bottom)
            else:
                return None, None
        else:
            return top, bottom + 1


def getApproximatePatternLocations(bwt, text, patterns, d):
    matchLocations = {}
    for pattern in patterns:
        # Break into seeds
        seeds = getPatternSeeds(pattern, d)

        validLocs = []

        for (s, seedShift) in seeds:
            first, last = BWMatchingRange(s, bwt)
            if first is None:
                continue
            else:
                locs = bwt.suffixArray[first:last]

            for l in locs:
                possStart = l - seedShift
                if possStart < 0:
                    continue
                possEnd = possStart + len(pattern)
                if possEnd > len(text):
                    continue
                if possStart in validLocs:
                    continue
                if isApproxMatch(pattern, text[possStart:possEnd], d):
                    validLocs.append(possStart)
        validLocs = list(set(validLocs))
        validLocs.sort()
        matchLocations[pattern] = validLocs

    return matchLocations