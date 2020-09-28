import random
#Take a random word from a txt file containing the SOWPODS dictionary.
file = open('C:\\py\\sowpods.txt', 'r')
word_list = file.readlines()
file.close()
wordList = []
for i in range(len(word_list)):
    wordList.append(word_list[i].strip())
HM_word = wordList[random.randint(0,len(wordList))]
#print(HM_word)
print('*+*+*+*HANGMAN*+*+*+*')
combin_list =''
incorrect_guesses = 0
guess_list = []
#Create a list of _ values to be filled in with correct guesses.
for letters in HM_word:
    guess_list.append('_')
while True:
    #get user input and put it in the same format as the target word (uppercase).
    x = input('Enter a guess: ')
    x = x.upper()
    #Fill in correct guesses
    for j in range(len(HM_word)):
        if HM_word[j] == x:
            guess_list[j] = x
    #Count incorrect guesses and end the game when you have no guesses left.
    if x not in HM_word:
        incorrect_guesses += 1
        if incorrect_guesses == 6:
            print(f'You are out of guesses, sorry! The word was {HM_word}.')
            break
        print(f'Wrong! You have {6-incorrect_guesses} incorrect guesses left.')
    for k in range(len(HM_word)):
        print(guess_list[k], end ='')
    print()
    #To check for a win we must convert the guess list (a list of single letters) to a string.
    combin_list = ''.join(guess_list)
    if combin_list == HM_word:
        print('Correct! Great Job!')
        break
