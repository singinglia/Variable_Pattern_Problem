
from BWT_assemble import YoungAvengersAssemble
from DouglasFunctions import validate

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


def runSmallTests():
    testcases, ans = readFile("Test one length 10 pattern.txt")
    exclusion = ["WVWVWVWVW", "XXXXXXXX"]
    l_min = 10
    m = .9

    # print(testcases[0])
    solutionList = []
    for test in testcases:
        patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min)
        validate(test, exclusion, m, l_min, idxes)




def runLongTests():
    testcases, ans = readFile("Test variable length 10 patterns.txt")
    exclusion = ["WVWVWVWVW", "XXXXXXXX"]
    l_min = 10
    m = .9


    for test in testcases:
        patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min)
        print(patterns)
        if not validate(test, exclusion, m, l_min, idxes):
            print("Test not passed")

    # print("DAG")
    # for s in solutionList:
    #     print(s)



if __name__ == '__main__':
    runLongTests()





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

