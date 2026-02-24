from inventory import load_servers, save_servers, INVENTORY_FILE, add_server

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
            if add_server(servers, hostname, ip_address):
                print(f"Success! Added {hostname}")
            else:
                print(f"Error, {hostname} already exists")

        elif choice == "2":
        #    for server in servers:
        #        print(server.hostname)
            print("list servers")
        elif choice == "3":
            print("toggle server")
        elif choice == "4":
            save_servers(INVENTORY_FILE, servers)
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Enter 1, 2, 3, or 4.")