

def patternSearch(I, E):
    #If Exclusion is short should we search it first?
    if len(E) < len(I):
        if isInExlusion(pattern, E):
            isFound = isInInclusion(pattern, I)
        else:
            if isInInclusion():
                isFound = isInExlusion()
    if isFound:
        #If we care about length we should do an extend step here like BLAST does,
        #But we actually don't right now, so is there any reason to search for 
        # #things longer than the the minimum number above match divisible by 4?
        #(This gives us no trailing)
        #Longer patterns = less future search space
        return pattern
    else:
        return  None

        


def isInExlusion():
    #We could use a bloom filter here, but only if we are
    #willing to look for just exact matches.
    #This might be valid as we  sort of moved away from finding actual primers

    #Otherwise we can just use the same code as inclusion and 
    #just pass in different string lists.


    #Returns Bool
    pass

def isInInclusion():
    #Either search the string 
    #Or possibly throw in the Burrows Wheeler Code
    pass

#Partition Patterns
def partitionInclusion():
    pass

class patternCache:
    def __init__(self):
        pass
    
    def add(self):
        pass

def getBestPatternList(I, E):
    #Should this be a condition or just set length?
    while some_amount_of_time:
        currPatternList = []
        modI = partitionInclusion()

        for ranges in modI:
            count = 0
            patternNotFound = True
            while patternNotFound and count >= 100:
                testPattern = getRandomPattern(ranges, ...)
                foundPattern = patternSearch(ranges, testPattern,...)
                if foundPattern is not None:
                    currPatternList.append(foundPattern)
                    patternCacheObj.add(foundPattern) 
                    patternNotFound = False
                count +=1

        #Search for patterns in gaps (New partition Edges)

    #Pick the best combos from library



if __name__ == '__main__':
    #Take in and process inclusion and exclusion

    bestPattern = getBestPatternList(I, E)
