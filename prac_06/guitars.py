from guitar import Guitar

def main():
    guitar_list = []
    print('My guitars!')
    name = input('Name: ')
    while name != '':
        year = input('Year: ')
        cost = input('Cost: $')
        guitar_add = Guitar(name, year, cost)
        guitar_list.append(guitar_add)
        print('{} added'.format(guitar_add))
        name = name = input('\nName: ')

    print('These are my guitars:')
    for i in range (0,len(guitar_list)):
        print('Guitar {}: {}'.format(i+1, guitar_list[i]))


main()

