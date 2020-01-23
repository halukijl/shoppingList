menuOption = None

mylist = []

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
    #print(menuOption)
    if menuOption == '1':
        print("Add item.")
    elif menuOption == '2':
        print("Print list.")
    elif menuOption == '3':
        print("Remove item by number.")
    elif menuOption == '4':
        print("Save list to file.")
    elif menuOption == '5':
        print("Load list from file.")
    elif menuOption == '6':
        print("Exit.")
    else:
        print("Your command was not recognized, please try again.")