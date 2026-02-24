from inventory import load_servers, save_servers, INVENTORY_FILE

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
            print("add server")
        elif choice == "2":
            print("list servers")
        elif choice == "3":
            print("toggle server")
        elif choice == "4":
            save_servers(INVENTORY_FILE, servers)
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Enter 1, 2, 3, or 4.")