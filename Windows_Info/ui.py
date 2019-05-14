import db
import misc_func
from objects import Computer

def main_menu():
    print("WELCOME TO WINDOWS 10 REFRESH PROGRAM!")
    print(" ")
    print("-" * 95)
    print("script - Powershell and Python functions")
    print("query - Database queries")
    print("exit - Exit the application")
    print("-" * 95)

def display_menu():
    print("Windows 10 Refresh Application")
    print(" ")
    print("COMMAND MENU")
    print("-" * 95)
    print("run - Run Powershell Script")
    print("read - Read text file")
    print("add - Add data to database")
    print("back - back to main menu")
    print("-" * 95)

def display_query_menu():
    print("QUERY MENU")
    print(" ")
    print("-" * 95)
    print("all - Shows all info")
    print("ram-a - Shows ram amount and slots")
    print("back - Back to main menu")
    print("-" * 95)
    

def main():
    db.connect()
    main_menu()
    while True:
        command_main = input("Please choose a menu: ").rstrip()
        if command_main == "script":
            display_menu()
            while True:
                command_script = input("Enter Command: ").rstrip()
                if command_script == "run":
                    misc_func.powershell()
                elif command_script == "read":
                    misc_func.read_text()
                elif command_script == "add":
                    misc_func.add_computer()
                elif command_script == "back":
                    main_menu()
                    break
                continue
        elif command_main == "query":
            display_query_menu()
            while True:
                command_query = input("Choose a query: ").rstrip()
                if command_query == "all":
                    print("Filler Text")
                elif command_query == "ram-a":
                    print("filler text")
                elif command_query == "back":
                    main_menu()
                    break
                continue
        elif command_main == "exit":
            break
        else:
            print("Not a Valid Command")
            main_menu()
    db.close()
    print("The application has closed succesfully")
    
if __name__ == "__main__":
    main()