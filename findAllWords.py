#Word finder, enter letters (either a word or random letters) to find all the words that can be made from those letters.
file = open('C:\\py\\sowpods.txt', 'r')
word_list = file.readlines()
file.close()
#Getting a list off all words from dictionary, and removing newline characters:
wordList = []
for words in range(len(word_list)):
    wordList.append(word_list[words].strip())

#Getting user input and making it all caps to match dictionary entries:
userIn = input('Enter any combination of letters to see all the words that can be made out of it: ')
userIn = userIn.upper()

#Removing any words longer than the input string:
anyLongerWordsRemoved = []
for words in range(len(wordList)):
    if len(wordList[words]) <= len(userIn):
        anyLongerWordsRemoved.append(wordList[words])

#Removing any words that have letters not present in the user input:
onlyWordsFromInputLetters = []
for words in range(len(anyLongerWordsRemoved)):
    incorrectLetters = 0
    for letters in range(len(anyLongerWordsRemoved[words])):
        if anyLongerWordsRemoved[words][letters] not in userIn:
            incorrectLetters += 1
    if incorrectLetters == 0:
        onlyWordsFromInputLetters.append(anyLongerWordsRemoved[words])

#Removing any words that have more of a specific letter than the user input:
onlyWordsWithRightAmountLetters = []
for words in range(len(onlyWordsFromInputLetters)):
    tooManyLetters = 0
    for letters in range(len(userIn)):
        if onlyWordsFromInputLetters[words].count(userIn[letters]) > userIn.count(userIn[letters]):
            tooManyLetters += 1
    if tooManyLetters == 0:
        onlyWordsWithRightAmountLetters.append(onlyWordsFromInputLetters[words])

#Printing results:
print('There are ' + str(len(onlyWordsWithRightAmountLetters)) + ' words that can be made with those letters, here they are: ')
print(onlyWordsWithRightAmountLetters)
