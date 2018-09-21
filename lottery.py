import random

def generatelist(count):
    list = []
    for x in range(count):
        random_number = random.randint(0,49)
        if random_number not in list:
            list.append(random_number)
    return list

def start_game():
    print('Welcome to the Lottery Generator')
    print(generatelist(int(input('Please enter how many random numbers would you like to have: '))))

start_game()