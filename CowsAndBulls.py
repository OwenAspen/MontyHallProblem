import random

#Cows and bulls: Generates a 4 digit string, asks user for a 4 digit string,
#if the strings match, you win. Otherwise, for every matching digit
#in the same position of the string, you will get a cow. for every digit in both
#strings, but not in the same position, you get a bull.

guesses = 0
#Counts the number of guesses taken.
numToGuess = str(random.randint(1000,9999))
#Generates a random 4 digit number.
checkAgainst = []
for i in range(4):
    checkAgainst.append(int(numToGuess[i]))
#Converting the number to a list for checking the user input against
while True:
    #print(checkAgainst) #Print statement for testing, comment out to actually play
    cows = 0
    bulls = 0
    #Counters
    userIn = input('Enter a 4 digit number: ')
    userNumList = []
    for j in range(4):
        userNumList.append(int(userIn[j]))
    #User input converted to a list
    print(userNumList)
    if int(numToGuess) == int(userIn):
        guesses += 1
        print('Correct! You got the right answer in ' + str(guesses) + ' tries.')
        #Check for correct input(win)
        break
    for k in range(4):
        if checkAgainst[k] == userNumList[k]:
            cows += 1
        #Check for cows
        if checkAgainst[k] in userNumList:
            if checkAgainst[k] != userNumList[k]:
                bulls += 1
        #Check for bulls
    guesses += 1
    print('Cows: ' + str(cows))
    print('Bulls: ' + str(bulls))

