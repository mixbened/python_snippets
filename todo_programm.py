print 'Welcome to the ToDo Programm.'

keep = raw_input('Would you like to enter a Todo Task? (y/n): ').lower()
todos = {}

while keep == 'y':
    new = raw_input('Enter your Todo: ')
    print 'Your Todo task is: ' + new
    status = raw_input('Did you complete the task? (y/n): ')
    if(status == 'y'):
        status = True
    else:
        status = False
    todos[new] = status
    keep = raw_input('Would you like to enter a Todo Task? (y/n): ').lower()

print 'All your Todos: %s' %todos
