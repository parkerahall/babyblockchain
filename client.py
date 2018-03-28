import socket, threading, sys

MSG_SIZE = 512

class VerifyThread(threading.Thread):
    def __init__(self, client, sock):
        super(VerifyThread, self).__init__()
        self.client = client
        self.socket = sock

    def run(self):
        try:
            message = self.socket.recv(MSG_SIZE)
            while message != '\n' and message != '':
                bang_index = message.find('!')

                command = message[:bang_index]
                data = message[bang_index + 1:]

                if command == "CONFIRM":
                    print(self.client.last_hash())
                    self.socket.send(self.client.last_hash())
                elif command == "ADD":
                    self.client.add_hash(data)
                else:
                    print("IMPROPER MESSAGE FORMAT")
                message = self.socket.recv(MSG_SIZE)
        except:
            self.socket.close()

class AddThread(threading.Thread):
    def __init__(self, client, sock):
        super(AddThread, self).__init__()
        self.client = client
        self.socket = sock

    def run(self):
        try:
            message = raw_input("")
            while message != "GOODBYE" and message != '':
                self.socket.send(message)
                message = raw_input("")
            print("Client is now listen only")
        except:
            self.socket.close()

class Client:
    def __init__(self, ip, a_port, v_port):
        self.add_socket = socket.socket()
        self.verify_socket = socket.socket()
        self.ip = ip
        
        self.add_port = a_port
        self.verify_port = v_port
        
        self.block_hashes = []

    def add_hash(self, new_hash):
        self.block_hashes.append(new_hash)

    def last_hash(self):
        return self.block_hashes[-1]

    def handle_first_message(self):
        message = self.verify_socket.recv(MSG_SIZE)
        while message == '':
            message = self.verify_socket.recv(MSG_SIZE)
        bang_index = message.find('!')
        last_hash = message[bang_index + 1:]
        self.add_hash(last_hash)

    def run(self):
        try:
            self.verify_socket.connect((self.ip, self.verify_port))
            self.handle_first_message()

            vt = VerifyThread(self, self.verify_socket)
            vt.start()
            
            self.add_socket.connect((self.ip, self.add_port))
            at = AddThread(self, self.add_socket)
            at.start()
        except:
            self.verify_socket.close()
            self.add_socket.close()
            print("GOODBYE")

if __name__ == "__main__":
    add_port = 1200
    verify_port = 1201
    if len(sys.argv) == 3:
        add_port = int(sys.argv[1])
        verify_port = int(sys.argv[2])
    c = Client('localhost', add_port, verify_port)
    c.run()