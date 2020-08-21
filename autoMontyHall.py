import random
#The Monty Hall problem.
numExperiments = 1000000
winFirstGuess = 0
winSecondGuess = 0
#win counters
for experimentNum in range(numExperiments):
    #picking the 1 is a win, picking a 0 is a loss.
    doors = [1,0,0]
    random.shuffle(doors)
    #randomize the order.
    guess1 = random.randint(0,2)
    #make a guess
    reguess = random.randint(0,1)
    #decide if you want to guess again after being shown one incorrect answer.
    if reguess == 0:
        if doors[guess1] == 1:
            winFirstGuess += 1
        #result if not reguessing
    else:
        if doors[0] == 0:
            secondGuess = random.randint(1,2)
            if doors[secondGuess] == 1:
                winSecondGuess += 1
        if doors[2] == 0:
            secondGuess = random.randint(0,1)
            if doors[secondGuess] == 1:
                winSecondGuess +=1
    #result if you guess again.
print('After running ' + str(numExperiments) + ' simulations the results are:')
print('The winning percentage using the first guess is ' +str((winFirstGuess/numExperiments)*200)+'%')
print('The winning percentage using the second guess is ' +str((winSecondGuess/numExperiments)*200)+'%')
