import functools


def input_error(func):
   
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            
            return "Error: Give me name and phone please."
        except KeyError:
            
            return "Error: Contact not found."
        except IndexError:
            
            return "Error: Enter user name."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


@input_error
def parse_input(user_input: str) -> tuple[str, list[str]]:
   
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
   
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts: dict[str, str]) -> str:
   
    if not contacts:
        return "Contacts list is empty."
    return "\n".join([f"{n}: {p}" for n, p in contacts.items()])


def main() -> None:
    
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command_data = parse_input(user_input)
        
        if isinstance(command_data, str):
            print(command_data)
            continue
            
        command, args = command_data

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()