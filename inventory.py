from server import Server
import csv
from exceptions import DuplicateHostnameError, DuplicateIPError, InvalidIPError
import os

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
                                status=row["status"])
                                )
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

###
def validate_ip(ip_address):
    parts = ip_address.split(".")
    if len(parts) != 4:
        raise InvalidIPError(f"Invalid IP address: {ip_address}")
    for part in parts:
        if not part.isdigit():
            raise InvalidIPError(f"Invalid IP address: {ip_address}")
        if not 0 <= int(part) <= 255:
            raise InvalidIPError(f"Invalid IP address: {ip_address}")


def add_server(servers, hostname, ip_address):
    validate_ip(ip_address)
    for server in servers:
        if server.hostname == hostname:
            raise DuplicateHostnameError(f"{hostname} already exists.")
        if server.ip_address == ip_address:
            raise DuplicateIPError(f"{ip_address} already exists.")
    servers.append(Server(hostname, ip_address))
    return True

def list_servers(servers):
     if not servers:
          print("No servers found")
     for server in servers:
          print(server)

def toggle_server(servers, hostname, action):
      # server_tmp = None
    for server in servers:
         if server.hostname == hostname:
             if action == "start":
                 server.start()
             elif action == "stop":
                 server.stop()
             return server
    return None