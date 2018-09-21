print('Hey! Would you like to do some Operations with this Python Calculator?')

operation = input('What Operation do you want to do? (+, -, *, /)')
x = int(input('Type your first Operand'))
y = int(input('Type your second Operand'))

if(operation == '+'):
    print(x + y)
elif(operation == '-'):
    print(x - y)
elif(operation == '*'):
    print(x * y)
else:
    print(x / y)
