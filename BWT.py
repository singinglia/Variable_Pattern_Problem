import copy

def getSuffixArray(word):
    suffixes = []
    for i in range(len(word)):
        suffixes.append(word[i:])
        # print(word[i:])
    sufSort = [idx[0] for idx in sorted(enumerate(suffixes), key=lambda x: x[1])]

    return sufSort

class BWT:
    def __init__(self, text, C=None, k=None):

        if text[-1] != "$":
            text = text + "$"

        self.suffixArray = getSuffixArray(text)
        word = self.betterBW_Transform(text)

        self.lastCol = [i for i in word]
        self.firstCol = sorted(self.lastCol)
        self.firstSeen = self.buildFirstOccurances()
        print(self.firstSeen)

        if C is None:
            C = int(len(word) * .05)
            if C < 5:
                C = 5
        # Count spacing
        self.C = C
        self.countMap = self.buildPartialCountMap(C)

        # if k is None:
        #     k = int(len(word)*.05)
        # self.pSuffArray = getPartialSuffixArray(word, k)

    def betterBW_Transform(self, word):
        idxes = self.suffixArray
        transform = []
        for i in idxes:
            if i == 0:
                transform.append(word[len(word) - 1])
            else:
                transform.append(word[i - 1])
        return "".join(transform)

    def buildFirstOccurances(self):
        firstSeen = {}
        currLetter = None
        for i, letter in enumerate(self.firstCol):
            if currLetter != letter:
                firstSeen[letter] = i
                currLetter = letter
        return firstSeen

    def CountSymbol(self, idx, symbol):
        start = idx - int(idx % self.C)
        count = self.countMap[start][symbol]
        for i in range(start, idx):
            if self.lastCol[i] == symbol:
                count += 1
        return count

    def buildPartialSuffixArray(word, k):
        suffixes = []
        for i in range(len(word)):
            suffixes.append(word[i:])
            # print(word[i:])
        sufSort = [idx[0] for idx in sorted(enumerate(suffixes), key=lambda x: x[1])]
        return sufSort[0::k]

    def buildPartialCountMap(self, C):
        countMap = {}
        letterMap = {}
        for letter in set(self.lastCol):
            letterMap[letter] = 0
        countMap[0] = copy.deepcopy(letterMap)

        for i, letter in enumerate(self.lastCol):
            i = i + 1

            letterMap[letter] += 1
            count = letterMap[letter]

            if i % C == 0:
                countMap[i] = copy.deepcopy(letterMap)
        return countMap



