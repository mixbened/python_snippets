class Contact(object):
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


def add_contact(first_name, last_name, phone_number, email, list):
    new_contact = Contact(first_name, last_name, phone_number, email)
    list.append(new_contact)
    print(new_contact.first_name+' succesfully added to the Contact Book.')


def print_contacts(contact_list):
    for index, contact in enumerate(contact_list):
        print('')
        print('ID ' + str(index) + ' ' + contact.first_name)
    details = input('Do you want to see details of a Contact? (y/n): ')
    if details == 'y':
        index = int(input('Please provide the Index: '))
        selected_contact = contact_list[index]
        for attr, value in selected_contact.__dict__.items():
            print('%s: %s' %(attr, value))


def delete_contact(list):
    print('Please select the Contacts ID of the Contact you would like to delete')
    for index, contact in enumerate(list):
        print('ID '+ str(index) + contact.first_name + ' ' + contact.last_name )
    index = int(input('Please provide the Index: '))
    selected_contact = list[index]
    list.remove(selected_contact)


def edit_contact(contact_list):
    print('Please select the Contacts ID of the Contact you would like to edit')
    for index, contact in enumerate(contact_list):
        print('ID '+ str(index) + contact.first_name + ' ' + contact.last_name )
    index = int(input('Please provide the Index: '))
    selected_contact = contact_list[index]
    print('What would you like to edit?')
    list_keys = list(selected_contact.__dict__.keys())
    for prop in list_keys:
        print(prop)
    selected_prop = input('Type in which Property you want to edit: ')
    new_value = input('And what would you like to change %s to?: ' %str(selected_prop))
    setattr(selected_contact, selected_prop, new_value)
    print('You changed %s to %s.' %(selected_prop, new_value))


def main():
    contact_book = []
    print('Hey, this is your Contact Book.')
    while True:
        print('These are your Options: a) List your Contacts - b) add a Contact - c) edit your Contacts - d) delete a Contact')
        selection = input('What would you like to Do? (a/b/c/d)')
        if selection == 'a':
            print_contacts(contact_book)
        elif selection == 'b':
            add_contact(input('Enter a first Name: '), input('Enter a last Name: '), input('Enter Phone Number: '), input('Enter email: '), contact_book)
        elif selection == 'c':
            edit_contact(contact_book)
        elif selection == 'd':
            delete_contact(contact_book)
        if input('Do you want to continue? (y/n): ') == 'n':
            break

if __name__ == "__main__":
    main()