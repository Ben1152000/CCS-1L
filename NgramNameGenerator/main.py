from numpy.random import choice

#print("Please specify data file: ")
#data = [line.strip() for line in open(raw_input()).readlines()]
data = ["*" + line.strip() + "*" for line in open("france.txt").readlines()]

datatable = {}
for line in data:
    for length in range(len(line)):
        for index in range(len(line) - length):
            key = line[index : index + length + 1]
            try:
                datatable[key] += 1
            except:
                datatable[key] = 1

alphabet = []
for key in datatable.keys():
    for letter in key:
        if letter not in alphabet:
            alphabet += letter

# Weighted choice based on a dictionary:
def select(dictionary):
    return choice(a=dictionary.keys(), p=[float(count) / float(sum(dictionary.values())) for count in dictionary.values()])

# Combine each probability weighted by length

def increment(prev):
    incdict = {} # Dictionary to contain possible increments
    for index in range(len(prev)):
        weighting = 1.0 / pow(2.5, index + 1)
        for letter in alphabet:
            if (prev[index:] + letter) in datatable:
                print prev[index:] + letter
                if (prev + letter) not in incdict.keys():
                    incdict[prev + letter] = float(datatable[prev[index:] + letter]) * weighting
                else:
                    incdict[prev + letter] += float(datatable[prev[index:] + letter]) * weighting
    for i in [(key, round(incdict[key], 2)) for key in incdict.keys()]:
        print i
    return select(incdict)


def generate():
    new = "*"
    while len(new) == 1 or new[-1] != "*":
        new = increment(new)
    return new
    
print generate()
