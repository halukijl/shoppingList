menuOption = None

menuText = '''
1.) Add item
2.) Print list
3.) Remove item by number
4.) Save list to file
5.) Load list from file
6.) Exit
'''

while menuOption != '6':
    print(menuText)
    menuOption = input("Enter selection\n")
    print(menuOption)
    