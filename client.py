import hashlib, socket, threading, sys
import blockchain_messages_pb2 as pc
import baby_blockchain as bbc

MSG_SIZE = 512

class VerifyThread(threading.Thread):
    def __init__(self, client, sock):
        super(VerifyThread, self).__init__()
        self.client = client
        self.socket = sock

    def run(self):
        message = self.socket.recv(MSG_SIZE)
        while message != '\n' and message != '':
            if message == "VERIFY":
                self.socket.send(self.client.chain.hash())
            else:
                print("IMPROPER MESSAGE FORMAT")
            message = self.socket.recv(MSG_SIZE)

class UpdateThread(threading.Thread):
    def __init__(self, client, sock):
        super(UpdateThread, self).__init__()
        self.client = client
        self.socket = sock

    def run(self):
        message_bytes = self.socket.recv(MSG_SIZE)
        while message_bytes != '\n' and message_bytes != '':
            if message_bytes == "REVERT":
                self.client.chain.replace_last_block()
            else:
                update_message = pc.UpdateMessage()
                update_message.ParseFromString(message_bytes)
                if update_message.type == pc.UpdateMessage.ENTRY:
                    proto_entry = update_message.entry
                    entry = bbc.Entry.init_from_proto(proto_entry)
                    self.client.chain.add_data(entry)
                elif update_message.type == pc.UpdateMessage.BLOCK:
                    proto_block = update_message.block
                    prev_hash = str(proto_block.prev_hash)
                    self.client.chain.add_new_block(prev_hash)
                    for proto_entry in proto_block.entries:
                        entry = Entry.init_from_proto(proto_entry)
                        self.client.chain.add_data(entry)
                else:
                    print("IMPROPER MESSAGE FORMAT")
            print(self.client.chain)
            message_bytes = self.socket.recv(MSG_SIZE)

class AddThread(threading.Thread):
    def __init__(self, client, sock):
        super(AddThread, self).__init__()
        self.client = client
        self.socket = sock

    def run(self):
        message = raw_input("")
        while message != "GOODBYE" and message != '':
            sender, receiver, amount = message.split(',')
            amount = int(amount)
            entry = bbc.Entry(sender, receiver, amount)
            self.client.chain.add_data(entry)

            proto_entry = pc.Entry()
            proto_entry.sender = sender
            proto_entry.receiver = receiver
            proto_entry.amount = int(amount)
            entry_bytes = proto_entry.SerializeToString()

            self.socket.send(entry_bytes)

            print(self.client.chain)

            message = raw_input("")

class Client:
    def __init__(self, ip, connect):
        self.ip             =   ip
        self.connect_socket =   socket.socket()
        self.update_socket  =   socket.socket()
        self.verify_socket  =   socket.socket()
        
        self.connect_port   =   connect

    def handle_connect_message(self):
        connect_bytes = self.connect_socket.recv(MSG_SIZE)
        connect_message = pc.ConnectMessage()
        connect_message.ParseFromString(connect_bytes)
        self.update_port = connect_message.update
        self.verify_port = connect_message.verify
        self.client_id = connect_message.client_id

        proto_chain = connect_message.chain
        self.chain = bbc.Chain.init_from_proto(proto_chain, hash_func)

        self.connect_socket.send("SUCCESS")

    def run(self):
        self.connect_socket.connect((self.ip, self.connect_port))
        self.handle_connect_message()

        self.verify_socket.connect((self.ip, self.verify_port))
        vt = VerifyThread(self, self.verify_socket)
        vt.start()
        
        self.update_socket.connect((self.ip, self.update_port))
        ut = UpdateThread(self, self.update_socket)
        ut.start()
        at = AddThread(self, self.update_socket)
        at.start()

def hash_func(inp):
    return hashlib.sha256(inp).hexdigest()

if __name__ == "__main__":
    connect_port = 1200
    if len(sys.argv) == 2:
        connect_port = int(sys.argv[1]) * 1200
    c = Client('localhost', connect_port)
    c.run()