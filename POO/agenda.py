class Agenda: 
    def __init__(self):
        self.username = None
        self.usernumber = None
        self.contacts = []

    def add_contact(self):
        name = input('Type contact\'s name: ')
        number = int(input('Type contact\'s number: '))
        for contact in self.contacts:
            if contact.number == number:
                print(f'Number already added!')
                return 
        while True:
            validation = input(f'Are you sure you want to add this contact? (yes/no) ')
            if validation.lower() == 'yes':
                self.contacts.append(Contact(name, number))
                print('contact created')
                return
            elif validation.lower() == 'no':
                print('contact was not created')
                return
            else:
                print('error, enter a valid input')
        
    def del_contact(self):
        number = int(input('Type the contact\'s number you want to delete: '))
        for contact in self.contacts:
            if contact.number == number:
                while True:
                    validation = input(f'Are you sure you want to delete this contact permanently? (yes/no) ')
                    if validation.lower() == 'yes':
                        self.contacts.remove(contact)
                        print('contact deleted')
                        return
                    elif validation.lower() == 'no':
                        print('contact was not deleted')
                        return
                    else:
                        print('error, enter a valid input')
        print('this contact does not exist')

    def update_contact(self):
        number = int(input('Type the contact\'s number that you want to replace: '))
        newnumber = int(input('Type the new number: '))
        newname = input('Type the new name: ')
        for contact in self.contacts:
            if contact.number == number:
                contact.number = newnumber
                contact.name = newname
                print('contact updated')
                return
        print('contact not found')

    def update_profile(self):
        username = input('Type your new name: ')
        number = int(input('Type your new number: '))
        self.username = username
        self.usernumber = number
        print(f'Profile updated! Name: {self.username}, Number: {self.usernumber}')
    
    def show_contacts(self):
        for contact in self.contacts:
            print(contact.name, contact.number)
        

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    

agenda = Agenda()
exec = True

while exec:
    option = int(input(' 1 - Add Contact \n 2 - Update Contact \n 3 - Delete Contact \n 4 - Update Profile \n 5 - Show Contacts \n 6 - Stop \n '))
    match option:
        case 1:
            agenda.add_contact()
        case 2:
            agenda.update_contact()
        case 3: 
            agenda.del_contact()
        case 4:
            agenda.update_profile()
        case 5:
            agenda.show_contacts()
        case 6:
            exec = False
        case _:
            print('Invalid option')