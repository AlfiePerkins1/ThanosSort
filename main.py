import random

def checkIfSorted(randomList, totalNum):
    count = 0
    for i in range (len(randomList) -1):
        if randomList[i] < randomList[i+1]:
            count += 1

    if count == totalNum - 1:
        print(f"List succesfully sorted with {len(randomList)} items")
        for i in range(len(randomList)):
            print(randomList[i])
    else:
        thanosSort(randomList, totalNum)


def thanosSort(randomList, totalNum):
    toRemove = len(randomList) / 2
    i = 0
    while i < toRemove:
        indexToRemove = random.randint(0,len(randomList))
        randomList.pop(indexToRemove-1)
        i+=1
    checkIfSorted(randomList, len(randomList))

if __name__ == '__main__':
    randomList = []
    totalNum = 100
    for i in range(0,totalNum):
        randomList.append(random.randint(1,150))
    checkIfSorted(randomList, totalNum)
