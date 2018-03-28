import hashlib, socket, threading, sys
import blockchain_messages_pb2

MSG_SIZE = 512

class AddThread(threading.Thread):
    def __init__(self, chain, sock):
        super(AddThread, self).__init__()
        self.chain = chain
        self.socket = sock

    def run(self):
        try:
            data = self.socket.recv(MSG_SIZE)
            while data != '\n' and data != '':
                self.chain.add_data(data.strip())
                print(self.chain)
                data = self.socket.recv(MSG_SIZE)
        finally:
            self.socket.close()

class StartThread(threading.Thread):
    def __init__(self, chain, sock):
        super(StartThread, self).__init__()
        self.chain = chain
        self.socket = sock

    def run(self):
        try:
            last_block = self.chain.last_block.string_to_hash()
            last_hash = self.chain.hash_func(last_block)
            message = "ADD!" + last_hash
            print("FIRST MESSAGE SENT")
            self.socket.send(message)
        except:
            self.socket.close()

class Server:
    def __init__(self, block_size, num_zeros, serve, verify, mine):
        self.chain = 

    def serve(self):
        threads = []

        verifier = socket.socket()
        verifier.bind(('localhost', self.verify_port))
        verifier.listen(1)

        server = socket.socket()
        server.bind(('localhost', self.serve_port))
        server.listen(1)

        try:
            while True:
                v, _ = verifier.accept()
                st = StartThread(self, v)
                st.start()
                self.verify_list.append(v)

                client, addr = server.accept()
                ip, port = addr
                print("CONNECTION MADE AT " + ip + ": " + str(port))

                at = AddThread(self, client)
                threads.append(at)
                at.start()
        finally:
            server.close()
            print("\nGOODBYE")

def hash_func(inp):
    return hashlib.sha256(inp).hexdigest()

if __name__ == "__main__":
    d = {"a": 1, "b": 2}
    serve_port = 1200
    verify_port = 1201
    mine_port = 1202
    if len(sys.argv) == 4:
        serve_port = int(sys.argv[1])
        verify_port = int(sys.argv[2])
        mine_port  = int(sys.argv[3])
    c = Chain(hash_func, 3, 2, serve_port, verify_port, mine_port)
    c.serve()



