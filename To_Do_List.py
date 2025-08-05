# List to store descriptions in memory
description_list = []

# Flag to control program loop
program_running = True


def main_menu():
    #Display the main menu.
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a new description")
    print("2. View current descriptions")
    print("3. Remove a description")
    print("4. Load descriptions from file")
    print("5. Exit")


def add_description():
    #Add a new description and auto-save
    description = input("Enter the description: ").strip()
    if description:
        description_list.append(description)
        save_to_file()
        print(f"Description '{description}' added and saved.")
    else:
        print("Description cannot be empty.")


def view_descriptions():
    #View current descriptions.
    if not description_list:
        print("No descriptions found.")
    else:
        print("\nYour current descriptions:")
        for index, desc in enumerate(description_list, start=1):
            print(f"{index}. {desc}")


def remove_description():
    #Remove a description by its number and auto-save
    view_descriptions()
    if description_list:
        try:
            number = int(input("Enter description number to remove: "))
            if 1 <= number <= len(description_list):
                removed_desc = description_list.pop(number - 1)
                save_to_file()
                print(f"Description '{removed_desc}' removed and saved.")
            else:
                print("Invalid description number.")
        except ValueError:
            print("Please enter a valid number.")


def save_to_file():
    #Save the current descriptions to a file.
    with open("tasks.txt", "w") as file:
        for index, desc in enumerate(description_list, start=1):
            file.write(f"{index}. {desc}\n")


def load_from_file():
    #Load descriptions from a file into memory.
    try:
        description_list.clear()
        with open("tasks.txt", "r") as file:
            for line in file:
                if line.strip():
                    desc_text = line.strip().split(". ", 1)[-1]
                    description_list.append(desc_text)
        print("Descriptions loaded from file.")
    except FileNotFoundError:
        print("No saved descriptions found.")


def __main__():
    #Main program loop.
    global program_running
    while program_running:
        main_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_description()
            elif choice == 2:
                view_descriptions()
            elif choice == 3:
                remove_description()
            elif choice == 4:
                load_from_file()
            elif choice == 5:
                print("Exiting program.")
                program_running = False
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


# Load descriptions at program start
load_from_file()

# Run the program
__main__()