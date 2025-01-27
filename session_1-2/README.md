# Python Programming Exercises

#### Exercise 1: Development Environment Setup
1. Create a dedicated folder for your code
2. Test that everything works by writing a simple "Hello, World!" program.

*hint: use the `print` function*


#### Exercise 2: Number Guessing Game
1. Create a file named `guess.py`
2. Program should have a secret number
3. Ask the user to input their guess
4. Tell the user if they got it right or wrong

*hint: use the function `input()` to get the users input*

**Extensions**:
- Make the secret number random
- Give the player multiple attempts
- Add hints (too high/too low)
- Keep track of the number of guesses

#### Exercise 3: Finding the Largest Number
1. Create a file named `largest_number.py`
2. The program should prompt the user for list of numbers seperated by whitespace
3. Find and print the largest number in the list

*hint: strings can be split by using .split(" "). also, remember to convert the user input into a number: `int(USER_INPUT)`*

#### Exercise 4: Grade Calculator
1. Create a file named `check_score.py`
2. Accept a score as input
3. Convert scores to letter grades using this scale:
   - **A**: 90 or above
   - **B**: 80-89
   - **C**: 70-79
   - **D**: 60-69
   - **F**: Below 60

**Extension**:
- Modify the program so that it accepts multiple scores (seperated by whitespace) and prints the grade for each score.

#### Exercise 5: Hangman Game
1. Create a file named `hangman.py`, copy the code below into it and run the program.
2. The code will contain some errors. Read them and try to fix them


**Extension**
- Modify the code so that `secret_word` isn't fixed but instead changes every time you run the program.

*hint: for the extension take a look at the function `random.choice` and try to figure out what it does.*

```python
import random

name = input('What is your name? ')
print('Hello, ' + name + '. Time to play hangman!')
print('Start guessing...')

secret_word = 'secret'
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in secret_word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1

    if failed == 0:
        print('\nYou won!')
        break

    print()
    guess = _______('guess a character: ')

    if len(guess) > 1:
        print('Only one character at the time, please!')
        continue

    guesses += guess 

    if guess not in ______:
        turns -= 1
        print('Wrong\n')
        print('You have', turns, 'more guesses')
        if turns == 0:
            print('You lose!')
```
