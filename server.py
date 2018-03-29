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
                if self.chain.is_full():
                    last_block = self.chain.current_block
                    last_hash = self.chain.hash_func(last_block)
                    self.confirm_hash(last_hash)
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
    def __init__(self, chain, serve, verify, mine):
        self.chain = chain
        self.serve_port = serve
        self.verify_port = verify
        self.mine_port = mine

        self.miner = self.init_miner()
        self.verify_list = []

    def init_miner(self):
        mine_server = socket.socket()
        mine_server.bind(('localhost', self.mine_port))
        mine_server.listen(1)

        miner, addr = mine_server.accept()
        ip, port = addr
        print("MINER AT " + ip + ": " + str(port))

        return miner

    def confirm_hash(self, h):
        total = len(self.verify_list)
        verified = 0
        for client in self.verify_list:
            client.send("CONFIRM")
            hash_check = client.recv(MSG_SIZE)
            if hash_check == h:
                verified += 1
        return verified == total
    
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
                st = StartThread(self.chain, v)
                st.start()
                self.verify_list.append(v)

                client, addr = server.accept()
                ip, port = addr
                print("CONNECTION MADE AT " + ip + ": " + str(port))

                at = AddThread(self.chain, client)
                threads.append(at)
                at.start()
        finally:
            server.close()
            print("\nGOODBYE")

def hash_func(inp):
    return hashlib.sha256(inp).hexdigest()

if __name__ == "__main__":
    serve_port = 1200
    verify_port = 1201
    mine_port = 1202
    if len(sys.argv) == 4:
        serve_port = int(sys.argv[1])
        verify_port = int(sys.argv[2])
        mine_port  = int(sys.argv[3])
    c = Chain(hash_func, 3, 2)
    s = Server(c, server_port, verify_port, mine_port)
    s.serve()



