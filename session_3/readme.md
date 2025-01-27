# Code Exercises

## Introduction
Below are some approachable but not necessarily trivial exercises. Generally
speaking, they can all be solved in 1-5 lines of code. The goal of today is 
to write some minimal coding, but perhaps more importantly, to reflect
on how these simple computations work in a logical way. Using this we will
slowly move to the world of "AI" and reflect on how this is modeled and solved.

To ease the process, I have provided two python files here in this repository.
Namely, `exercises.py` and `run_tests.py`. The first one contains contains some
erroneous code that you'll need to fix based on the descriptions below. The latter
is a simple script you can call from the terminal to test if your implementations
work out (`python run_tests.py`).

## Get Started
You can get the code by copy-pasting it from the browser, downloading each individual file or by cloning the repository from the commandline. The easiest way is probably to go to the root of the repository: [click here](https://github.com/danielvarab/udk-exercises) and click on code > "Download ZIP". Unpack the zip file and open it with your favorite code editor.

*Alternatives:*
- `git clone https://github.com/danielvarab/udk-exercises`
- go to https://github.com/danielvarab/udk-exercises/tree/main/session_3 and click on each file respectively, and hit the download button in the upper right corner.


## Instructions

There are 5 exercises to solve and the main idea is to approach them twice.
1. First, using your newly aquired skills in python - verify your solutions by running `python run_tests.py`.
2. Using the magical power of large language models (LLMs). To solve these tasks, please use this [link (todo!)](todo)

For starters, I'd recommend you solve the programming step without the help of ChatGPT and others. You can solve the exercises in any order you'd like, but you should try to complete all of them. Please don't hesitate to ask for help if you get stuck!

## Exercises

### Exercise 1
Write a function `price_with_taxes(price, tax_rate)` that takes in two arguments: `price` and `tax_rate`. The function should return the price with taxes included. Assume that the tax rate is given as a percentage (meaning between 0 and 1).

An example. If the price is 10 (euros perhaps) and the tax rate is 20%, then the function should return the number 12.
```python
# exercise 1
def price_with_taxes(price, tax_rate):
    raise NotImplementedError()
```

### Exercise 2
Write a function `length_of_name(first_name, last_name)` that takes in two arguments: `first_name` and `last_name`. The function should return the length of the combined name, including white space between them (this means the whitespace is implicite). Assume that the names are given as strings.

```python
def length_of_name(first_name, last_name):
    raise NotImplementedError()
```

### Exercise 3
Write a function `bitcoin_price_in_euros(bitcoin_amount)` that takes in one argument: `bitcoin_amount`. The function should return the price of the Bitcoin amount in euros. Assume that the Bitcoin price is given as a constant and that the conversion rate from dollars to euros is given by the constant `DOLLAR_TO_EURO_RATE`.

*hint: Use constants to pass the tests by their name, e.g. BITCOIN_PRICE*

```python
BITCOIN_PRICE = 99125.17192690  # 27th of January
DOLLAR_TO_EURO_RATE = 0.95
def bitcoin_price_in_euros(bitcoin_amount):
    # you have access to two variables here:
    #  - BITCOIN_PRICE
    #  - DOLLAR_TO_EURO_RATE
    raise NotImplementedError()
```

### Exercise 4
Write a function `last_character_third_word(string)` that takes in one argument: `string`. The function should return the last character of the third word in the string. Assume that the words are given as a list of strings.

*hint: remember you can split strings using the string function split() and that you can index into lists, e.g. `random_list[5]`*

```python
def last_character_third_word(string):
    return NotImplementedError()
```

### Exercise 5
Write a function `compute_average(numbers)` that takes in one argument: `numbers`. The function should return the average of all the numbers in the list. Assume that the numbers are given as a list of integers.

*hint: remember you can use the built-in functions sum() and len()*

```python
def compute_average(numbers):
    return NotImplementedError()
```