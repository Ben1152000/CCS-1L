from numpy.random import choice

#print("Please specify data file: ")
#data = [line.strip() for line in open(raw_input()).readlines()]
data = ["*" + line.strip() + "*" for line in open("countries.txt").readlines()]

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

# Weighting function of n-gram count based on length:
def weighting(length):
    return pow(2, 1 - (20 * pow(length, -2)))

# Function to statistically generate a new letter on a string
def increment(prev):
    possibilities = {}
    # Define set of possibilities
    for letter in alphabet:
        possibilities[prev + letter] = 0.
    # Weight each of the possibilities
    for option in possibilities:
        for index in range(len(option)):
            if option[index:] in datatable:
                #print option[index:], datatable[option[index:]], round(weighting(len(option[index:])), 3), round(datatable[option[index:]] * weighting(len(option[index:])), 3)
                possibilities[option] += datatable[option[index:]] * weighting(len(option[index:]))

    return select(possibilities)

def generate():
    new = "*"
    while len(new) == 1 or new[-1] != "*":
        new = increment(new)
    return new

for i in range(50):
    g = generate()
    print g, g in data
