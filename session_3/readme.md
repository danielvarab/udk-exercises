# Code Exercises

Below are some approachable but not necessarily trivial exercises. Generally
speaking, they can all be solved in 1-5 lines of code. The goal of today is 
to write some minimal coding, but perhaps more importantly, to reflect
on how these simple computations work in a logical way. Using this we will
slowly move to the world of "AI" and reflect on how this is modeled and solved.

To ease the process, I have provided two python files here in this repository.
Namely, `exercises.py` and `run_tests.py`. The first one contains contains some
erroneous code that you'll need to fix based on the descriptions below. The latter
is a simple script you can call from the terminal to test if your implementations
work out.

There are 5 exercises to solve and the idea is to approach them twice.
1. First using newly aquired skills in python and validating your code using `run_tests.py`.
2. Using the magical power of large language models (LLMs). To solve these tasks, please use this [link (todo!)](todo)

For starters, I'd recommend you try to solve the programming without the help of ChatGPT or the likes. You can solve the exercises in any order you'd like, but you should try to complete all of them.

## Exercise 1
Write a function `price_with_taxes(price, tax_rate)` that takes in two arguments: `price` and `tax_rate`. The function should return the price with taxes included. Assume that the tax rate is given as a percentage.

An example. If the price is 10 (euros perhaps) and the tax rate is 20%, then the function should return the number 12.
```python
# exercise 1
def price_with_taxes(price, tax_rate):
    raise NotImplementedError()
```

## Exercise 2
Write a function `length_of_name(first_name, last_name)` that takes in two arguments: `first_name` and `last_name`. The function should return the length of the combined name, including white space between them (this means the whitespace is implicite). Assume that the names are given as strings.

```python
def length_of_name(first_name, last_name):
    raise NotImplementedError()
```

## Exercise 3
Write a function `bitcoin_price_in_euros(bitcoin_amount)` that takes in one argument: `bitcoin_amount`. The function should return the price of the Bitcoin amount in euros. Assume that the Bitcoin price is given as a constant and that the conversion rate from dollars to euros is given by the constant `DOLLAR_TO_EURO_RATE`.

*hint: Use constants to pass the tests by their name, e.g. BITCOIN_PRICE*

```python
def bitcoin_price_in_euros(bitcoin_amount):
    # you have access to two variables here:
    #  - BITCOIN_PRICE
    #  - DOLLAR_TO_EURO_RATE
    raise NotImplementedError()
```

## Exercise 4
Write a function `last_character_third_word(string)` that takes in one argument: `string`. The function should return the last character of the third word in the string. Assume that the words are given as a list of strings.

*hint: remember you can split strings using the function split()*

```python
def last_character_third_word(string):
    return NotImplementedError()
```


## Exercise 5
Write a function `compute_average(numbers)` that takes in one argument: `numbers`. The function should return the average of all the numbers in the list. Assume that the numbers are given as a list of integers.

*hint: remember you can use the built-in functions sum() and len()*

```python
def compute_average(numbers):
    return NotImplementedError()
```