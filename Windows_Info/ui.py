import db
import misc_func
import menu
from objects import Computer


def main():
    """Main Function Refrences all other functions and accepts user input"""
    db.connect()
    menu.main_menu()
    while True:
        command_main = input("Please choose a menu: ").rstrip()
        if command_main == "script":
            menu.display_menu()
            while True:
                command_script = input("Enter Command: ").rstrip()
                if command_script == "main":
                    misc_func.powershell()
                elif command_script == "delete":
                    misc_func.delete_disabled()
                elif command_script == "refresh":
                    misc_func.refresh_list()
                elif command_script == "disabled":
                    misc_func.get_disabled()
                elif command_script == "read":
                    misc_func.read_text()
                elif command_script == "back":
                    menu.main_menu()
                    break
                continue
        elif command_main == "query":
            menu.display_query_menu()
            while True:
                command_query = input("Choose a query: ").rstrip()
                if command_query == "all":
                    print("Filler Text")
                elif command_query == "os":
                    misc_func.format_select_os()
                elif command_query == "delete":
                    db.delete_computer()
                elif command_query == "test":
                    db.test()
                elif command_query == "back":
                    menu.main_menu()
                    break
                continue
        elif command_main == "exit":
            break
        else:
            print("Not a Valid Command")
            menu.main_menu()
    db.close()
    print("The application has closed succesfully")

if __name__ == "__main__":
    main()
