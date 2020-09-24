import random
#comparing a random search to find a number out of 100 with a binary search to find a number out of 100.
num_experiments = 10000
attemptsR = 0
attemptsB = 0
#This loop does the random searches.
for experiments in range(num_experiments):
    ans = random.randint(0,100)
    guess = random.randint(0,100)
    while guess != ans:
        guess = random.randint(0,100)
        attemptsR += 1
#This loop does the binary searches.
for experiments in range(num_experiments):
    list1 = list(range(0,100))
    low = 0
    mid = 50
    high = 100
    number = random.randint(0,99)
    while mid != number:
        if number > mid:
            low = mid
        if number < mid:
            high = mid
        mid = int((low+high)/2)
        attemptsB += 1

print(f'It took an average of {attemptsR/num_experiments} guesses to get the correct number using a random search.')
print(f'It took an average of {attemptsB/num_experiments} guesses to get the correct number using a binary search.')
