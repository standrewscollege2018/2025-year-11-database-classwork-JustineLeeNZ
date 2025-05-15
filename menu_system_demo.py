''' demo of a menu system - Phil Adams '''

run_program = True
while run_program == True:
    # Display menu
    print("Titanic Menu")
    print("1. Search by name\n2. Search by class\n3. Quit")

    # Get selection
    get_choice = True
    while get_choice == True:
        try:
            menu_choice = int(input())
            if menu_choice < 1 or menu_choice > 3:
                print("Enter a number from 1 to 3")
            else:
                get_choice = False
        except ValueError:
            print("Enter an integer")

    if menu_choice == 1:
        # Run search by name
        print("Search by name")


    elif menu_choice == 2:
        # Run search by class
        print("Search by class")

    else:
        run_program = False
