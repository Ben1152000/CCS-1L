from numpy.random import choice

names = []
with open("english.txt") as text:
    for line in text:
        names.append("^" + line.lower().strip() + "^")

letters = []
for name in names:
    for char in name:
        if char not in letters:
            letters.append(char)
print(letters)


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
    probabilities[l1]["value"] = 1


for name in names:
    for idx in range(len(name)):
        probabilities[name[idx]]["value"] += 1
    for idx in range(len(name) - 1):
        probabilities[name[idx]][name[idx + 1]]["value"] += 1
    for idx in range(len(name) - 2):
        probabilities[name[idx]][name[idx + 1]][name[idx + 2]]["value"] += 1
    for idx in range(len(name) - 3):
        probabilities[name[idx]][name[idx + 1]][name[idx + 2]][name[idx + 3]]["value"] += 1
    for idx in range(len(name) - 4):
        if [name[idx + 4]] in probabilities[name[idx]][name[idx + 1]][name[idx + 2]][name[idx + 3]].keys():
            probabilities[name[idx]][name[idx + 1]][name[idx + 2]][name[idx + 3]][name[idx + 4]]["value"] += 1
        else:
            probabilities[name[idx]][name[idx + 1]][name[idx + 2]][name[idx + 3]][name[idx + 4]] = {"value": 1}

def randKey(dictionary):
    values = [float(x) / sum(dictionary.values()) for x in dictionary.values()]
    return choice(dictionary.keys(), 1, p=values)[0]

def generate():
    name = "^"
    while len(name) < 2 or name[-1] != "^":
        aggregate = {}
        for letter in letters:
            aggregate[letter] = 0
        if len(name) > 3:
            for key in probabilities[name[-4]][name[-3]][name[-2]][name[-1]].keys():
                if (key != "value"):
                    aggregate[key] += probabilities[name[-4]][name[-3]][name[-2]][name[-1]][key]["value"] * 30000000
        if len(name) > 2:
            for key in probabilities[name[-3]][name[-2]][name[-1]].keys():
                if (key != "value"):
                    aggregate[key] += probabilities[name[-3]][name[-2]][name[-1]][key]["value"] * 1000000
        if len(name) > 1:
            for key in probabilities[name[-2]][name[-1]].keys():
                if (key != "value"):
                    aggregate[key] += probabilities[name[-2]][name[-1]][key]["value"] * 1000
        if len(name) > 0:
            for key in probabilities[name[-1]].keys():
                if (key != "value"):
                    aggregate[key] += probabilities[name[-1]][key]["value"]
        name += randKey(aggregate)
    return name


for i in range(10):
    print(generate())

