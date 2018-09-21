greeting = 'y'

while greeting == 'y':
    type = raw_input('Would you like to convert kmh or miles? (kmh/miles): ')
    value = int(raw_input('Type in the Value that you want to convert: '))
    if(type == 'kmh'):
        print str(value*0.62137) + 'mi'
        greeting = raw_input('Do you want to convert a number? (y/n)')
    elif(type == 'miles'):
        print str(value*(1/0.62137)) + 'km/h'
        greeting = raw_input('Do you want to convert a number? (y/n)')
    else:
        print 'Enter correct type!'
        greeting = raw_input('Do you want to convert a number? (y/n)')
