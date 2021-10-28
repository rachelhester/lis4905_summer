import random
random.seed()

def myGrades(grade, value): #tuple
    myTuple = (grade, value)
    return myTuple 

myDict = dict()
nameSet = {"Justin Davis","Philip Bowman","Sebastian Angel-Riano","Alexander Boehm","Andrew Vargas","Rachel Hester","Mitchell Mujwit","Bryan Humphries"}
mySet = set()


def myGrades(grade, name): #tuple
    myTuple = (name, grade)
    return myTuple 

for name in nameSet:
    if random.random() > 0.50:
        myDict[name] = "S"
    else:
        myDict[name] = "U"

for name in myDict:
    name = name
    grade = myDict[name]
    myTuple = myGrades(name, grade)
    mySet.add(myTuple)

for Sentence in mySet:
    print(f"{Sentence[1]} : {Sentence[0]}")