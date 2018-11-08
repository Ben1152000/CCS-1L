from numpy.random import choice

# Generate random letter from dict

def getNamesList(file):
    names = []
    with open(file) as text:
        for line in text:
            names.append("^" + line.lower().strip() + "^")
    return names

def findLetters(names):
    letters = []
    for name in names:
        for char in name:
            if char not in letters:
                letters.append(char)
    return letters

def genProbDict(names, letters):
    probabilities = {}
    for l1 in letters:
        probabilities[l1] = {}
        for l2 in letters:
            probabilities[l1][l2] = {}
            for l3 in letters:
                probabilities[l1][l2][l3] = {}
                for l4 in letters:
                    probabilities[l1][l2][l3][l4] = {}
                    probabilities[l1][l2][l3][l4]["value"] = 0
                probabilities[l1][l2][l3]["value"] = 0
            probabilities[l1][l2]["value"] = 0
        probabilities[l1]["value"] = 0
    for name in names:
        for idx in range(len(name)):
            if (name[idx] in letters):
                probabilities[name[idx]]["value"] += 1
        for idx in range(len(name) - 1):
            if (name[idx] in letters and name[idx + 1] in letters):
                probabilities[name[idx]][name[idx + 1]]["value"] += 1
        for idx in range(len(name) - 2):
            if (name[idx] in letters and name[idx + 1] in letters and name[idx + 2] in letters):
                probabilities[name[idx]][name[idx + 1]][name[idx + 2]]["value"] += 1
        for idx in range(len(name) - 3):
            if (name[idx] in letters and name[idx + 1] in letters and name[idx + 2] in letters and name[idx + 3] in letters):
                probabilities[name[idx]][name[idx + 1]][name[idx + 2]][name[idx + 3]]["value"] += 1
    return probabilities

def getMaxLength(stringList):
    maxLength = 0
    for name in NAMES:
        if len(name) > maxLength:
            maxLength = len(name)
    return maxLength

def getPosLocDict(names, letters):
    maxLength = getMaxLength(letters)
    positiveList = []
    for i in range(maxLength):
        positiveList.append({})
        for letter in letters:
            positiveList[i][letter] = 0
        for name in names:
            try:
                positiveList[i][name[i]] += 1
            except:
                pass
    return positiveList

def getNegLocDict(names, letters):
    maxLength = getMaxLength(letters)
    negativeList = []
    for i in range(maxLength):
        negativeList.append({})
        for letter in letters:
            negativeList[i][letter] = 0
        for name in names:
            try:
                negativeList[i][name[-(i + 1)]] += 1
            except:
                pass
    return negativeList

DATABASE = "england.txt" # Training database
NAMES = getNamesList(DATABASE) # List of all names in training database
LETTERS = findLetters(NAMES) # Find the list of all letters
PROBDICT = genProbDict(NAMES, LETTERS) # Find the probabilities of series of letters
NEGLOCDICT = getNegLocDict(NAMES, LETTERS) # Find the probabilities of letters from the end of names
POSLOCDICT = getPosLocDict(NAMES, LETTERS) # Find the probabilities of letters from the beginning of names
LETTERS.remove("^")

def randKey(dictionary):
    values = [float(x) / sum(dictionary.values()) for x in dictionary.values()]
    return choice(dictionary.keys(), 1, p=values)[0]

def scale(dictionary, factor):
    for key in dictionary.keys():
        dictionary[key] = dictionary[key] * factor
    return dictionary

def sumDict(dictionary):
    count = 0
    for val in dictionary.values():
        count += val
    return count

def addDicts(dictionaries, keys):
    sumDictionary = {}
    for key in keys:
        sumDictionary[key] = 0
        for dictionary in dictionaries:
            try:
                sumDictionary[key] += dictionary[key]
            except:
                pass
    return sumDictionary

def next(string, letters, length):
    if len(string) == 0 or length - len(string) < 2: # Return ^ if at the start or end of string
        return "^"
    # Create probability dictionaries
    thirdLevel = {}
    if len(string) >= 3:
        for key in letters:
            thirdLevel[key] = PROBDICT[string[-3]][string[-2]][string[-1]][key]["value"]
    secondLevel = {}
    if len(string) >= 2:
        for key in letters:
            secondLevel[key] = PROBDICT[string[-2]][string[-1]][key]["value"]
    firstLevel = {}
    for key in letters:
        firstLevel[key] = PROBDICT[string[-1]][key]["value"]
    baseLevel = {}
    for key in letters:
        baseLevel[key] = PROBDICT[key]["value"]
    startLevel = POSLOCDICT[len(string)]
    endLevel = NEGLOCDICT[length - len(string)]
    # Scale dictionaries to be equal in magnitude
    if sumDict(baseLevel) > 0:
        scale(baseLevel, 1.0 / sumDict(baseLevel)).values()
    if sumDict(firstLevel) > 0:
        scale(firstLevel, 10.0 / sumDict(firstLevel)).values()
    if sumDict(secondLevel) > 0:
        scale(secondLevel, 500.0 / sumDict(secondLevel)).values()
    if sumDict(thirdLevel) > 0:
        scale(thirdLevel, 10000.0 / sumDict(thirdLevel)).values()
    if sumDict(startLevel) > 0:
        if len(string) == 1:
            scale(startLevel, 1000000.0 / (sumDict(startLevel))).values()
        else:
            scale(startLevel, 1.0 / (sumDict(startLevel))).values()
    if sumDict(endLevel) > 0:
        scale(endLevel, 100000.0 / (sumDict(endLevel) * 2 ** (length - 2 - len(string)))).values()

    print(int(sumDict(baseLevel)), int(sumDict(firstLevel)), int(sumDict(secondLevel)), int(sumDict(thirdLevel)), int(sumDict(startLevel)), int(sumDict(endLevel)))

    # Calculate aggregate probabilities and execute
    sumLevel = addDicts([baseLevel, firstLevel, secondLevel, thirdLevel, startLevel, endLevel], letters)
    return randKey(sumLevel)

length = 20
generated = ""
while len(generated) < 2 or generated[-1] != "^":
    generated += next(generated, LETTERS, length)
print(generated)

