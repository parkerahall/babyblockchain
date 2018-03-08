import hashlib, socket, threading, sys

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
            self.socket.send(message)
        except:
            self.socket.close()

class Block:
    def __init__(self, prev_hash, size):
        self.data       = []
        self.prev_hash  = prev_hash
        self.max_size   = size
        self.status     = "OPEN"

    @staticmethod
    def genesis_block(block_size):
        return Block("FIRST BLOCK", block_size)

    def add_data(self, data):
        if self.status == "OPEN":
            self.data.append(data)
            if len(self.data) == self.max_size:
                self.status = "CLOSED"

    def string_to_hash(self):
        return self.prev_hash + str(self)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

class Chain:
    def __init__(self, hash_func, block_size, num_zeros, serve, verify, mine):
        self.hash_func      =   hash_func
        self.block_size     =   block_size
        self.num_zeros      =   num_zeros
        self.serve_port     =   serve
        self.verify_port    =   verify
        self.mine_port      =   mine

        self.chain          =   [Block.genesis_block(block_size)]
        self.last_block     =   self.chain[0]
        self.lock           =   threading.Lock()

        self.miner          =   self.init_miner()
        self.verify_list    =   []

    def init_miner(self):
        mine_server = socket.socket()
        mine_server.bind(('localhost', self.mine_port))
        mine_server.listen(1)

        miner, addr = mine_server.accept()
        ip, port = addr
        print("MINER AT " + ip + ": " + str(port))

        return miner

    def add_data(self, data):
        self.lock.acquire()
        self.check_block_status()
        self.last_block.add_data(data)
        self.lock.release()

    def check_block_status(self):
        if self.last_block.status == "CLOSED":
            self.next_block()

    def next_block(self):
        prefix = '0' * self.num_zeros

        last_hash = self.hash_func(self.last_block.string_to_hash())
        good_hash = self.confirm_hash(last_hash)
        if good_hash:
            print("VERIFIED")
            string_zeros = str(self.num_zeros)

            self.miner.send(string_zeros + '!' + last_hash)
            
            nonce = self.miner.recv(MSG_SIZE)
            while nonce != '\n' and nonce != '':
                test_hash = self.hash_func(last_hash + nonce)
                if test_hash[:self.num_zeros] == prefix:
                    break
                nonce = self.miner.recv(MSG_SIZE)

            new_block = Block(test_hash, self.block_size)
            self.chain.append(new_block)
            self.last_block = new_block
        else:
            prev_hash = self.last_block.prev_hash
            new_block = Block(prev_hash, self.block_size)
            self.last_block = new_block

    def confirm_hash(self, h):
        total = len(self.verify_list)
        verified = 0
        for client in self.verify_list:
            client.send("CONFIRM!")
            hash_check = client.rcv(MSG_SIZE)
            if hash_check == h:
                verified += 1
        return verified == total

    def current_block(self):
        return self.last_block

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

                client, addr = server.accept()
                ip, port = addr
                print("CONNECTION MADE AT " + ip + ": " + str(port))

                at = AddThread(self, client)
                threads.append(at)
                at.start()
        finally:
            server.close()
            print("\nGOODBYE")

    def __str__(self):
        block_strings = [str(x) for x in self.chain]
        return '\n'.join(block_strings)

    def __repr__(self):
        return self.__str__()

def hash_func(inp):
    return hashlib.sha256(inp).hexdigest()

if __name__ == "__main__":
    serve_port = 1200
    verify_port = 1201
    mine_port = 1202
    if len(sys.argv) == 3:
        serve_port = int(sys.argv[1])
        verify_port = int(sys.argv[2])
        mine_port  = int(sys.argv[2])
    c = Chain(hash_func, 3, 2, serve_port, verify_port, mine_port)
    c.serve()



