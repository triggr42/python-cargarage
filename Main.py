from UI import UI


def main():

    myui = UI()

    myui.read_data_store()

    while True:
        myui.display_garage_contents()
        myui.display_menu_options()

        option = myui.get_menu_choice().upper()
        if option == 'A':
            myui.add_car()
        elif option == 'D':
            myui.remove_car()
        elif option == 'H':
            myui.hire_out()
        elif option == 'R':
            myui.return_car()
        elif option == 'U':
            myui.write_data_store()
        elif option == 'X':
            response = input('Are you sure you want to quit the Carnucopia application, Y or N?').upper()
            if response == 'Y':
                break
        else:
            print('You need to enter one of the menu options')
            pass
    print('Goodbye')


# Checking that this is the start of the program
if __name__ == '__main__':
    main()















