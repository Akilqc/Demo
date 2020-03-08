import time
import random
print('Welcom to the game')
temp = input('Guess which number is in my mind: ')
guess = int(temp)
secret = random.randint(1,11)
n = 0
while guess != secret and n < 2:
    if guess > secret:
        print('You Foolish,It\'s smaller than what you guess\n\n')
    else:
        print('You Foolish,It\'s bigger than what you guess\n\n')
    time.sleep(1)
    if n != 1:
        print('You still have ',2-n,' chance to guess!\n')
    else:
        print('This is your last chance!')
    temp = input('Try again: ')
    guess = int(temp)
    n += 1
time.sleep(1)
if n==2:
    print('Game over the answer is:',secret)
else:
    print('\nGame Over')