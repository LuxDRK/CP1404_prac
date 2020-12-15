def main():
    email_to_name = {}
    email = input('Email: ')
    while email != '':
        name = get_name(email)
        if input('Is your name {}? (Y/n) '.format(name)).lower() in ('','y','yes'):
            email_to_name[email] = name
        else:
            email_to_name[email] = input('Name: ')
        email = input('Email: ')
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))

def get_name(email):
    name_list = (email.split('@')[0]).split('.')
    name = ' '.join(name_list).title()
    return name

main()