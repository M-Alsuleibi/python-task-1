class Server:
    def __init__(self, hostname, ip_address, status="stopped"):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status

    def start(self):
        self.status = "running"
        
    def stop(self):
        self.status = "stopped"

