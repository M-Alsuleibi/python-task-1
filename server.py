class Server:
    def __init__(self, hostname, ip_address, status="stopped"):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"
    # to be used in list_servers print statement
    def __repr__(self):
            return (
                f"Hostname: {self.hostname} | "
                f"IP: {self.ip_address} | "
                f"Status: {self.status}"
            )
