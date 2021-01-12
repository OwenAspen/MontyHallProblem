from pathlib import Path
import random
#Word Scramble. Change the word_length variable to adjust difficulty
word_length = 5
open_file =  Path('C:/py/sowpods.txt')
file = open(open_file,'r')
raw_dictionary = file.readlines()
file.close()
full_dictionary = []
#removing newline characters from input file
for entries in raw_dictionary:
    full_dictionary.append(entries.strip())
#creating a list of correct length seed words
def pick_word_list(word_length, word_list):
    trimmed_dictionary = []
    for word in word_list:
        if len(word) == word_length:
            trimmed_dictionary.append(word)
    return trimmed_dictionary
#finding all the words that can be made from the seed word
def all_possibe_words_from_seed(seed):
    #Removing any words longer than the seed word:
    anyLongerWordsRemoved = []
    for words in range(len(full_dictionary)):
        if len(full_dictionary[words]) <= len(seed):
            anyLongerWordsRemoved.append(full_dictionary[words])
    #Removing any words that have letters not present in the seed word:
    onlyWordsFromInputLetters = []
    for words in range(len(anyLongerWordsRemoved)):
        incorrectLetters = 0
        for letters in range(len(anyLongerWordsRemoved[words])):
            if anyLongerWordsRemoved[words][letters] not in seed:
                incorrectLetters += 1
        if incorrectLetters == 0:
            onlyWordsFromInputLetters.append(anyLongerWordsRemoved[words])
    #Removing any words that have more of a specific letter than the seed word:
    onlyWordsWithRightAmountLetters = []
    for words in range(len(onlyWordsFromInputLetters)):
        tooManyLetters = 0
        for letters in range(len(seed)):
            if onlyWordsFromInputLetters[words].count(seed[letters]) > seed.count(seed[letters]):
                tooManyLetters += 1
        if tooManyLetters == 0:
            onlyWordsWithRightAmountLetters.append(onlyWordsFromInputLetters[words])
    return onlyWordsWithRightAmountLetters
#randomizing the seed word
def word_randomizer(word):
    while True:
        chars = list(word)
        random.shuffle(chars)
        randomized = ''.join(chars)
        if randomized != word:
            return randomized
        else: 
            continue
#making a list of blanks to represent unfound words
def blank_list_maker(word_list):
    hidden_list = word_list.copy()
    for i in range(len(word_list)):
        hidden_list[i] = 'X'*len(word_list[i])
    return hidden_list
#game loop
game_counter = 0
while True:
    trimmed_dictionary = []
    trimmed_dictionary = pick_word_list(word_length, full_dictionary)
    seed_word = trimmed_dictionary[random.randint(0, len(trimmed_dictionary))]
    possible_words = []
    possible_words = all_possibe_words_from_seed(seed_word)
    possible_words.sort(key=len, reverse=True)
    blanks_list = blank_list_maker(possible_words)
    shuffled_seed = word_randomizer(seed_word)
    while True:
        print(shuffled_seed)
        #print(possible_words)
        print(blanks_list)
        user_in = input('Enter a guess or \'?\' to shuffle the letters: ')
        user_in = user_in.upper()
        if user_in == '?':
            shuffled_seed = word_randomizer(seed_word)
        if user_in in blanks_list:
            print(blanks_list)
            continue
        elif user_in in possible_words:
            blanks_list.append(possible_words[possible_words.index(user_in)])
            blanks_list.remove('X'*len(user_in))
            blanks_list.sort(key=len, reverse=True)
        if set(blanks_list) == set(possible_words):
            game_counter += 1
            break
    print(blanks_list)
    print('\n***YOU GOT ALL THE WORDS! GREAT JOB!***\n')
    if game_counter > 0:
        play_again = input('Play again? (enter \'n\' to quit or \'y\' to play again): ')
        if play_again == 'n':
            break
if game_counter == 1:
    print('\nYou played 1 game.')
if game_counter > 1:
    print(f'\nYou played {game_counter} games.')
print('\nThanks for playing!')
