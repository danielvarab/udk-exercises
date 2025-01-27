import random

# CONSTANTS
BITCOIN_PRICE = 99125.17192690  # 27th of January
DOLLAR_TO_EURO_RATE = 0.95


# exercise 1
def price_with_taxes(price, tax_rate):
    return price * (1 + tax_rate)
    raise NotImplementedError()


# exercise 2
def length_of_name(first_name, last_name):
    return len(first_name + " " + last_name)
    raise NotImplementedError()


# exercise 3
def bitcoin_price_in_euros(bitcoin_amount):
    return (bitcoin_amount * BITCOIN_PRICE) / DOLLAR_TO_EURO_RATE
    raise NotImplementedError()


# exercise 4
def last_character_third_word(string):
    words = string.split(" ")
    return words[2][-1]
    return NotImplementedError()


# exercise 5
def compute_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
    return NotImplementedError()
