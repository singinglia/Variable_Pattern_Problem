
from BWT_assemble import YoungAvengersAssemble
from DouglasFunctions import validateBWT
# from data_generation import genData
from timing import *

def readFile(testFile, incluLength=5, get=None):
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
        if get is not None:
            if len(answers) > get:
                f.close()
                return testCases[get], answers[get]
    f.close()
    return testCases, answers


def runSmallTests():
    testcases, ans = readFile("Test one length 10 pattern.txt")
    exclusion = ["WVWVWVWVW", "XXXXXXXX"]
    l_min = 10
    m = .8

    # print(testcases[0])
    solutionList = []
    for test in testcases:
        patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min)
        validateBWT(test, exclusion, m, l_min, idxes)




def runLongTests():
    testcases, ans = readFile("Test variable length 10 patterns.txt")
    exclusion = ["WVWVWVWVWVWVWVWVWVWVWVWVWVWV", "XXXXXXXXXXXXXXXXXXXXXXXX"]
    l_min = 10
    m = .8

    passedCount = 0
    start = time.time()
    for i, test in enumerate(testcases):
        patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min)
        # print(patterns)
        # print(i)
        if not validateBWT(test, exclusion, m, l_min, idxes, patterns):
            print("Test not passed")
        else:
            passedCount += 1
    print("Passed:", passedCount)
    end = time.time()
    print("Run time:", end - start)


    # print("DAG")
    # for s in solutionList:
    #     print(s)

def crazyDataRun():
    test, ans = readFile("Test many variably lengthed patterns.txt", incluLength=50, get=1)
    exclusion = ["WVWVWVWVWVWVWVWVWVWVWVWVWVWV", "XXXXXXXXXXXXXXXXXXXXXXXX"]
    l_min = 15
    m = .8

    # start = time.time()
    # print(time.asctime(time.localtime(time.time())))
    # test = [x[:3000] for x in test]
    patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min)
    # end = time.time()
    # print("Run time:", end - start)

    print("Patterns:")
    print(len(patterns))
    print(patterns)




if __name__ == '__main__':
    # runLongTests()
    crazyDataRun()

    #genData(num_strings, len_strings, len_pattern, num_patterns, num_muts)


