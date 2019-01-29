# Class for a server


class fprint:
    @staticmethod
    def cmd(string, prefix="[$] ", suffix="", end="\n"):
        print(prefix + string + suffix, end=end)


class Identifier:
    def __init__(self):
        self.re = __import__("re")

    def is_ip(self, obj):
        if self.is_string(obj):
            real_ip = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
            return self.re.match(real_ip, obj)
        return False

    def is_port(self, obj):
        if self.is_integer(obj):
            return 0 <= obj <= 255
        return False

    @staticmethod
    def is_string(obj):
        return isinstance(obj, str)

    @staticmethod
    def is_integer(obj):
        return isinstance(obj, int)

"""
Main Server module
Server(server_ip="", server_port="")    - Sets up the server variable
Server.start()                          - Starts the Server.listener() and Server.responder() threads

Other Server modules
Server.get_server_ip()                  - Returns server IP
Server.set_server_ip(new_server_ip)     - Sets a new server IP
Server.get_server_port()                - Returns server Port
Server.set_server_port(new_server_port) - Sets a new server Port

Private Server modules
Server.listener()                       - 
Server.responder()                      - 
"""
class Server:
    def __init__(self, server_ip=None, server_port=None):
        # Modules
        self.identify = Identifier()
        self.thread = __import__("_thread")

        # Server variables
        self.server_ip = None
        self.set_server_ip(server_ip)
        self.server_port = None
        self.set_server_port(server_port)

    def get_server_ip(self):
        return self.server_ip

    def set_server_ip(self, new_server_ip):
        if self.identify.is_ip(new_server_ip):
            self.server_ip = new_server_ip

    def set_server_port(self, new_server_port):
        if self.identify.is_port(new_server_port):
            self.server_port = new_server_port

    def start(self):
        self.thread.start_new_thread(self.listener, ())
        self.thread.start_new_thread(self.responder, ())

    def listener(self):
        is_running = True
        while is_running:
            pass

    def listener_user(self, socket, ip, port):

    def responder(self):
        is_running = True
        while is_running:
            pass