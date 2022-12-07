list_1 = ['sumit', 'satyam', 'bhupinder', 'sonu', 'vikash',  'nagendra', 'priya', 'ganesh',]
list_2 = ['7254970701', '8432343201', '9353453530', '6542354353',  '996348751',  '8797703454','6655443322', '930689057']
while(True):
    print('welcome to the Repositary')
    print(20 * '-')

    print('1. Display list')
    print('2. Search contact')
    print('3. Exit\n')

    a = int(input('option no.>> '))

    if(a == 1):
        print('  Names       Contacts', end='\n')
        for i in range(len(list_1)):
            print(str(i+1)+'.' + list_1[i], ' --> ', list_2[i])
    elif(a == 2):
        search = input('Search name: ')
        search = search.lower()
        if search in list_1:
            print('Contact =', list_2[list_1.index(search)])
        else:
            print('Person not found')
    elif(a == 3):
        break
    else:
        print('!!! Invalid option !!!')
        continue

    print('\r')