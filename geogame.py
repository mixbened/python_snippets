import random

country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna"}

def start_game():
    random_number = random.randint(0,2)
    country = list(country_capital_dict.keys())[random_number]
    answer = country_capital_dict[country]
    guess = input('What is the Capital of %s?: ' %country)
    if answer == guess:
        print('Thats correct!')
    else:
        print('Thats wrong!')


def geogame():
    print('Welcome to the Capital guessing Game!')
    keep_guessing = True
    while keep_guessing:
        start_game()
        if input('Do you want to continue? (y/n)') != 'y':
            break
