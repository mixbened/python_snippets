from random import randint

print 'Welcome to the Number guessing Game, I already have a Number in Mind.'

x = randint(0,9)

while True:
    guess = int(raw_input('Guess a Number!'))
    if(guess == x):
        print 'Correct!'
        break
    else:
        if(guess > x):
            print 'The Secret Number is lower'
        else:
            print 'The Secret Number is higher'
