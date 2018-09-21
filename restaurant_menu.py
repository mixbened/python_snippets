menu_file = open('menu.txt', 'w')

print 'This is your Menu Program.'

menu = {}

while True:
    keep = raw_input('Do you want to enter a dish? (y/n): ')
    if(keep == 'y'):
        dish = raw_input('Put in the Dish: ')
        price = raw_input('What should it cost?: ')
        menu[dish] = float(price)
    else:
        menu_file.write(str(menu))
        menu_file.close()
        break
