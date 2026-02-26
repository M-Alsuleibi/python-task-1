from inventory import load_servers, save_servers, INVENTORY_FILE, add_server, list_servers, toggle_server
from exceptions import DuplicateHostnameError, DuplicateIPError, InvalidIPError

def show_menu():
    print("\n--- Server Inventory Menu ---")
    print("1. Add a new server")
    print("2. List all servers")
    print("3. Toggle server status")
    print("4. Exit")

def get_choice():
    return input("\nEnter choice: ").strip()

def run():
    servers = load_servers(INVENTORY_FILE)

    while True:
        show_menu()
        choice = get_choice()

        if choice == "1":
            hostname = input("Enter hostname: ").strip()
            ip_address = input("Enter ip address: ").strip()

            if not hostname or not ip_address:
                print("Error, empty value not accepted")
                continue

            try:
                add_server(servers, hostname, ip_address)
                print(f"Success! Added {hostname}.")
            except InvalidIPError as e:
                print(f"Error: {e}")
            except DuplicateHostnameError as e:
                print(f"Error: {e}")
            except DuplicateIPError as e:
                print(f"Error: {e}")

        elif choice == "2":
           list_servers(servers)

        elif choice == "3":
            hostname = input("Enter the hostname of the server to toggle: ").strip()
            action = input("Type 'start' or 'stop': ").strip()

            if action != "start" and action != "stop":
                print("Error: status must be 'start' or 'stop'")
                continue
            # server could be Server or None, called once, result stored
            server = toggle_server(servers, hostname, action)

            if not server:
                print("server not found")
                continue
            # here the type checker knows that server is passed the (if not server) guard
            # no AttributeError
            print(f"Success! {hostname} is now {server.status}.")

        elif choice == "4":
            save_servers(INVENTORY_FILE, servers)
            print("Goodbye!")
            break

        else:
            print("Error: Invalid choice. Enter 1, 2, 3, or 4.")