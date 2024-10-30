class Contact:
    def __init__(self,name,work_phone,personal_phone,work_email,personal_email):
        self.name = name
        self.work_phone = work_phone
        self.personal_phone = personal_phone
        self.work_email = work_email
        self.personal_email = personal_email

class Contacts:
    def __init__(self):
        self.view = 'quit'
        self.contact_list = []
        self.choice = None
        self.index = None

    def display(self):
        while True:
            if self.view == 'list':
                self.show_list()
            elif self.view == 'info':
                self.show_info()
            elif self.view == 'add':
                self.add_contact()
            elif self.view == 'quit':
                print('\nClosing the contact list..')
                break

        def show_list(self):
            print('Contact List:')
            for i, contact in enumerate(self.contact_list):
                print(f'{i+1}. {contact.name}')

    def show_info(self):
        if self.index is not None and 0 <= self.index < len(self.contact_list):
            contact = self.contact_list[self.index]
            print(f'Name: {contact.name}')
            print(f'Work Phone: {contact.work_phone}')
            print(f'Personal Phone: {contact.personal_phone}')
            print(f'Work Email: {contact.work_email}')
            print(f'Personal Email: {contact.personal_email}')
        else:
            print('Invalid contact index.')

    def add_contact(self):
        name = input('Enter name: ')
        work_phone = input('Enter work phone number: ')
        personal_phone = input('Enter personal phone number: ')
        work_email = input('Enter work email: ')
        personal_email = input('Enter personal email: ')
        self.contact_list.append(Contact(name, work_phone, personal_phone, work_email, personal_email))

if __name__ == '__main__':
    contacts = Contacts()
    contacts.display()