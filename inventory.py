from server import Server
import csv

INVENTORY_FILE = "inventory.csv"
CSV_FIELDNAMES = ["hostname", "ip_address", "status"]


def load_servers(filepath):
    try:
        servers = []

        with open(filepath, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                servers.append( Server(
                                hostname=row["hostname"],
                                ip_address=row["ip_address"],
                                status=row["status"],)
                                )
                print(row)
        return servers
    except FileNotFoundError:
                print("Loading inventory... No existing inventory.csv found. Starting fresh.")
                return []
    except (KeyError):
            print(f"Warning: Could not parse {filepath}. Starting fresh.")
            return []

def save_servers(filepath, servers):
    try:
        with open(filepath, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDNAMES)
            writer.writeheader()
            for server in servers:
                writer.writerow({
                    "hostname": server.hostname,
                    "ip_address": server.ip_address,
                    "status": server.status,
                })

    except OSError as e:
         print(f"Error: Could not write to {filepath}: {e}")

def add_server(servers, hostname, ip_address):
    for server in servers:
        if server.hostname == hostname:
            return False
    servers.append(Server(hostname, ip_address))
    return True

