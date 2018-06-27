import random
from math import ceil
import sys
WORDS = ['super','turbulent','racecar','elephant']

def try_guessing():
    
    secretword = random.choice(WORDS)
    guess = ''    
    tries = ceil(len(secretword) * 1.20)
    
    output = ["_"]*len(secretword)
    
    used = []
    
    print("Your Word is Chosen: ", output)

    while True:
        found = False
        yield
        guess = yield guess
        
        for l, letter in enumerate(guess):
            
            if letter not in used:
                used.append(letter)
                for i, trueLetter in enumerate(secretword):
                    if letter == trueLetter:
                        output[i] = letter
                        found = True
                tries -= 1
            else:
                print("You have already used the letter: {}".format(letter))
        
        if found:
            print("Letters discovered:",output)
        else:
            print("No new discoveries:")
        
        if '_' not in output:
            print('You have solved the puzzle! {}'.format(''.join(output)) )
            raise StopIteration()
        elif tries == 0:
            print('Too bad, you have no more tries.  Your word was: {}'.format(''.join(secretword)))
            raise StopIteration( )

def guess_wrapper():
    yield from try_guessing()
    

def word_guesser():
    print("Welcome to word guesser.")
    guesses = guess_wrapper()
    guesses.send(None)
    for _ in guesses:
        try:
            guesses.send(input("Your next letter please: ").strip())
        except StopIteration:
            if input("Would you like to play again (y/n)? ").lower() == 'y':
                word_guesser()
    sys.exit()
if __name__ == '__main__':
    word_guesser()