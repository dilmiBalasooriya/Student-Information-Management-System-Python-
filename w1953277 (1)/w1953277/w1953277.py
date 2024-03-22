#!/usr/bin/python

import os
                      
creditscreditRange = [0, 20, 40, 60, 80, 100, 120]

CreditatLevel = [[120, 0, 0, ], [100, 20, 0], [100, 0, 20], [80, 40, 0], [80, 20, 20], [80, 0, 40], [60, 60, 0],
                        [60, 40, 20], [60, 20, 40], [60, 0, 60], [40, 80, 0], [40, 60, 20], [40, 40, 40], [40, 20, 60],
                        [40, 0, 80], [20, 100, 0], [20, 80, 20], [20, 60, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100],
                        [0, 120, 0], [0, 100, 20], [0, 80, 40], [0, 60, 60], [0, 40, 80], [0, 20, 100], [0, 0, 120]]


userId = ""
DeferScore = 0
FaiScore = 0

progress = 0
progressTrailer = 0
moduleRetriever = 0
countExclude = 0
overallComes = 0



progressionStatus = ["Progress", "Progress(module trailer)", "Progress(module trailer)",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Exclude", "Do not progress-module retriever",
                       "do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Exclude", "Exclude",
                       "Do not progress-module retriever", "Do not progress-module retriever",
                       "Do not progress-module retriever", "Do not progress-module retriever", "Exclude", "Exclude",
                       "Exclude"]


UserInput = []
volume = []
volumes = []
listPro = []
listCv = []
studentId = []
studentRecords = {}



def progressFileRead(file):
    try:
        file_progression_R = open(file, 'a')
        for x in file_progression_R.readlines():
            listPro.append(x)
        file_progression_R.close()
    except Exception as e:
        print(e)


def readVolumeFile(file):
    try:
        filevolume = open(file, "a")
        for x in filevolume.readlines():
            listCv.append(x) 
        filevolume.close()
    except Exception as e:
        print(e)


def writeData():
    global UserInput
    try:
        with open('User.txt', 'w+') as f:
            for line in UserInput:
                f.write('%s\n' % line)

        with open('volume.txt', 'w+') as f:
            for line in volume:
                f.write('%s\n' % line)

    except Exception as e:
        print(e)



progressFileRead("User.txt")
readVolumeFile("volume.txt")


def detailsDetails():
    try:
        print("--------------------------------------------------")
        for x in listPro:
            print("Progress Results : ", x, "Sum of Credit : ", listCv[listPro.index(x)],
                  "--------------------------------------------------\n", end='')
    except Exception as e:
        print(e)


while True:
    try:
        userId = input('\nPlease enter your ID : ')
        # collecting scores at pass
        PassCredits = int(input('\nPlease enter your credits at pass: '))
        #determining if the entered value falls within the creditRange
        creditRange = PassCredits in creditscreditRange
        if creditRange:
            # getting credits at defer
            DeferScore = int(input('Please enter your credits at defer: '))
            #determining if the entered value falls within the creditRange
            creditRange = DeferScore in creditscreditRange
            if creditRange:
                # getting credits at fail
                FaiScore = int(input('Please enter your credits at fail: '))
                #Checking whether the entered number is in the creditRange
                creditRange = FaiScore in creditscreditRange
                if creditRange:
                    # count total
                    totalScore = PassCredits + DeferScore + FaiScore

                    if totalScore == 120:
                        #get credit volumes
                        volumes = [PassCredits, DeferScore, FaiScore]
                        volumesAvailability = volumes in CreditatLevel

                        if volumesAvailability:

                            volumeId = CreditatLevel.index(volumes)
                         
                            progressionType = progressionStatus[volumeId]
                            print(progressionType)

                            # part 2 support >>>>
                            UserInput.append(progressionType)
                            volume.append(volumes)
                            studentId.append(userId)

                            progress = UserInput.count("Progress")
                            progressTrailer = UserInput.count("Progress(module trailer)")
                            moduleRetriever = UserInput.count("Do not progress-module retriever")
                            countExclude = UserInput.count("Exclude")
                            overallComes = int(len(UserInput))
                            

                            # <<<<<< part 2 support


                            while volumesAvailability:
                                print("\nWould you like to enter another set of credits?")
                                loop_or_not = input("Enter 'y' for yes or 'q' for quit and view results:")
                                loop_or_not = loop_or_not.upper()
                                if loop_or_not == 'YES' or loop_or_not == 'Y':
                                    iscontinue = True
                                elif loop_or_not == 'QUIT' or loop_or_not == 'Q':
                                    iscontinue = False
                                else:
                                    print("\u001b[31mPlease enter valid input!\u001b[0m")
                                    continue
                                break
                        if iscontinue:
                            continue
                        else:
                            break
                    else:
                        print("\u001b[31m\nTotal credit incorrect !\u001b[0m")
                else:
                    print("\u001b[31m\nCredit value Out of creditRange !\u001b[0m")
            else:
                print("\u001b[31m\nCredit value Out of creditRange !\u001b[0m")
        else:
            print("\u001b[31m\nCredit value Out of creditRange !\u001b[0m")
    except Exception as e:
        print("\u001b[31m\nInteger value required!\u001b[0m")
        print(e, "\n")


os.system('cls')

print(f'''
             -----Histogram-----\n
        Progress Module    ->   {progress}   :   {'*' * progress}
        Trailer  Module    ->   {progressTrailer}   :   {'*' * progressTrailer}
        Retriever Module   ->   {moduleRetriever}   :   {'*' * moduleRetriever}
        Exclude  Module    ->   {countExclude}   :   {'*' * countExclude}
        Total outcomes     -> : {overallComes}
\n=============================================================
''')



# part 2
print("\n---<<<<< part 2 >>>>>---\n")
# print output from list.
for i in range(overallComes):
    print(UserInput[i], " : ", volume[i])



# Part 3 - Text File
print("\n\n---<<<<< part 3 >>>>>---\n")
writeData()
detailsDetails()



# Part 4 – Dictionary
print("\n\n---<<<<< part 4 >>>>>---\n")
for i in studentId:
    studentRecords[i] = str(UserInput[studentId.index(i)]), str(
        volume[studentId.index(i)])

# get output from Dictionary
for x in studentRecords:
    print(x, " : ", studentRecords[x])
