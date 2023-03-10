
from BWT_assemble import YoungAvengersAssemble

def readFile(testFile, incluLength=5):
    f = open(testFile, "r")
    testCases = []
    testSet = []
    answers = []
    count = 0
    for i, line in enumerate(f):
        if count == incluLength:
            testCases.append(testSet)
            count = 0
            answers.append(line.rstrip().split())
            testSet = []
        else:
            testSet.append(line.rstrip())
            count += 1
    f.close()
    return testCases, answers


if __name__ == '__main__':

    testcases, ans = readFile("Test one length 10 pattern.txt")
    exclusion = ["WVWVWVWVW", "XXXXXXXX"]
    l_min = 10
    m = .9

    # print(testcases[0])
    solutionList = []
    for test in testcases:
        possPatterns = YoungAvengersAssemble(test, exclusion, m, l_min)
        solutionList.append(possPatterns)

    print("Possible Patterns")
    for s in solutionList:
        print(s)

    # start = time.time()
    # bestPatternList, indexLists = AvengersAssemble(testcases[1], exclusion, m, l_min)
    # end = time.time()
    #
    # print("Run time:", end-start)
    # print("Best Pattern List")
    # print(len(bestPatternList))
    # print(bestPatternList)
    # print(indexLists)
    #
    # validate(inclusion, exclusion, m, l_min, indexLists)
    #
    #
    #
    # bestPatternList, indexLists = AvengersAssemble(inclusion, exclusion, m, l_min, t=100)
    #
    #
    # print("Exclusion")
    # print(exclusion)
    # print("Best Pattern List")
    # print(len(bestPatternList))
    # print(bestPatternList)

    # print(inclusion)
    # print(exclusion)
    # print(m)
    # print(l_min)
    #
    # print(indexLists)

