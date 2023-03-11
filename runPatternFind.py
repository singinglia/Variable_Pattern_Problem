
from BWT_assemble import YoungAvengersAssemble
from DouglasFunctions import validateBWT
# from data_generation import genData
from timing import *
import pandas as pd

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

import math
def runSmallTests():
    exclusion = ["WVWVWVWVWVWVWVWVWVWVWVWVWVWV", "XXXXXXXXXXXXXXXXXXXXXXXX"]
    l_min = 10
    m = .8
    runFile("Test variable length 10 patterns.txt", 5, exclusion, l_min, m, "Small_Res_k10.txt")

def runLargeTests():
    exclusion = ["WVWVWVWVWVWVWVWVWVWVWVWVWVWV", "XXXXXXXXXXXXXXXXXXXXXXXX"]
    l_min = 15
    m = .75
    runFile("Test medium variably lengthed patterns.txt", 10, exclusion, l_min, m, "Medium_Res_k15.txt")

def runFile(fileName, incluLen, exclusion, l_min, m, writeFile, doPartition = False):
    testcases, ans = readFile(fileName, incluLength=incluLen)
    df = pd.DataFrame()

    passedCount = 0
    dataCol = []
    for i, test in enumerate(testcases):
        print("Started ", i)
        dataCol.append(i)
        dataCol.append(m)
        dataCol.append(l_min)
        start = time()
        patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min, partition=doPartition)
        end = time()
        dataCol.append(end-start)
        # if not validateBWT(test, exclusion, m, l_min, idxes, patterns):
        #     print("Test not passed")
        # else:
        #     passedCount += 1
        dataCol.append(len(patterns))
        expectedNum = math.ceil(len(test[0])/45)
        dataCol.append(expectedNum)
        dataCol.append(len(test[0]))
        # dataCol.append(passedCount)
        # print(dataCol)
        df[i] = dataCol
        dataCol = []
    df = df.transpose()
    mapping = {df.columns[0] :'ID_NUM', df.columns[1] : 'Match_Prop',
               df.columns[2]: 'L_Min', df.columns[3] : 'Run_time',
               df.columns[4]: 'Patterns_Found', df.columns[5] :'Expected_Patterns',
               df.columns[6]: "Length of Input Strings"}
    df = df.rename(columns=mapping)
    df.to_csv(writeFile)
    return df

def bigDataRun(id, m, l_min):
    test, ans = readFile("Test many variably lengthed patterns.txt", incluLength=50, get=id)

    dataCol = []
    dataCol.append(id)
    dataCol.append(m)
    dataCol.append(l_min)
    start = time()

    patterns, idxes = YoungAvengersAssemble(test, exclusion, m, l_min)

    end = time()
    dataCol.append(end - start)
    # if not validateBWT(test, exclusion, m, l_min, idxes, patterns):
    #     print("Test not passed")
    # else:
    #     passedCount += 1
    dataCol.append(len(patterns))
    expectedNum = math.ceil(len(test[0]) / 45)
    dataCol.append(expectedNum)
    dataCol.append(len(test[0]))
    return(dataCol)

def bigDataDF(runRangeMin, runRangeMax, writeFile):
    df = pd.DataFrame()
    m = .75
    l_min = 15
    for i in range(runRangeMin, runRangeMax):
        newCol = bigDataRun(i, m, l_min)
        df[i] = newCol

    df = df.transpose()
    mapping = {df.columns[0] :'ID_NUM', df.columns[1] : 'Match_Prop',
               df.columns[2]: 'L_Min', df.columns[3] : 'Run_time',
               df.columns[4]: 'Patterns_Found', df.columns[5] :'Expected_Patterns',
               df.columns[6]: "Length of Input Strings"}
    df = df.rename(columns=mapping)
    df.to_csv(writeFile)


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
    # runSmallTests()
    runLargeTests()
    # mediumDF = runLargeTests()
    # crazyDataRun()
    bigDataDF(2,4, "crazy_data_res.csv")

    #genData(num_strings, len_strings, len_pattern, num_patterns, num_muts)


