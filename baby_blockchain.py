import threading
import blockchain_messages_pb2 as pc

class Entry:
    def __init__(self, ff, tt, amount):
        self.ff = ff
        self.tt = tt
        self.aa = amount

    @staticmethod
    def init_from_proto(proto):
        ff = proto.sender
        tt = proto.receiver
        aa = proto.amount
        return Entry(ff, tt, aa)

    def __str__(self):
        from_string = "From: " + self.ff
        to_string = "To: " + self.tt
        amount_string = "Amount: " + str(self.aa)
        return from_string + ', ' + to_string + ', ' + amount_string

    def __repr__(self):
        return self.__str__()

class Block:
    def __init__(self, prev_hash, size):
        self.data       = []
        self.prev_hash  = prev_hash
        self.max_size   = size
        self.is_full    = False

    @staticmethod
    def init_from_proto(proto):
        prev_hash = str(proto.prev_hash)
        block_size = proto.block_size
        return Block(prev_hash, block_size)

    @staticmethod
    def genesis_block(block_size):
        return Block("FIRST BLOCK", block_size)

    def add_data(self, data):
        if not self.is_full:
            self.data.append(data)
            if len(self.data) == self.max_size:
                self.is_full = True

    def string_to_hash(self):
        return self.prev_hash + str(self)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return self.data.__iter__()

    def __str__(self):
        return str([str(e) for e in self.data])

    def __repr__(self):
        return self.__str__()

class Chain:
    def __init__(self, blocks, block_size, hash_func):
        self.chain          =   blocks if blocks else [Block.genesis_block(block_size)]
        self.block_size     =   block_size
        self.lock           =   threading.Lock()

        self.hash_func = hash_func

    @staticmethod
    def init_from_proto(proto, hash_func):
        block_size = proto.block_size

        blocks = []
        for proto_block in proto.blocks:
            prev_hash = proto_block.prev_hash
            new_block = Block(prev_hash, block_size)
            for proto_entry in proto_block.entries:
                s = proto_entry.sender
                r = proto_entry.receiver
                a = proto_entry.amount
                new_entry = Entry(s, r, a)
                new_block.add_data(new_entry)
            blocks.append(new_block)
        return Chain(blocks, block_size, hash_func)

    def add_data(self, data):
        self.lock.acquire()

        self.current_block().add_data(data)
        
        self.lock.release()

    def add_new_block(self, prev_hash):
        self.lock.acquire()

        assert(len(self.current_block()) == self.block_size)
        empty_block = Block(prev_hash, self.block_size)
        self.chain.append(empty_block)
        
        self.lock.release()

    def replace_last_block(self):
        self.lock.acquire()

        prev_hash = self.current_block().prev_hash
        replacement = Block(prev_hash, self.block_size)
        self.chain[-1] = replacement

        self.lock.release()

    def to_proto(self):
        proto_chain = pc.Chain()
        proto_chain.block_size = self.block_size
        for block in self.chain:
            proto_block = proto_chain.blocks.add()
            proto_block.prev_hash = block.prev_hash
            for entry in block:
                proto_entry = proto_block.entries.add()
                proto_entry.sender = entry.ff
                proto_entry.receiver = entry.tt
                proto_entry.amount = entry.aa
        return proto_chain

    def current_block(self):
        return self.chain[-1]

    def is_full(self):
        return self.current_block().is_full

    def hash(self):
        block_hashes = [b.string_to_hash() for b in self.chain]
        print(block_hashes)
        return self.hash_func(str(block_hashes))

    def last_block_hash(self):
        hash_string = self.current_block().string_to_hash()
        return self.hash_func(hash_string)

    def __str__(self):
        block_strings = [str(x) for x in self.chain]
        return '\n'.join(block_strings)

    def __repr__(self):
        return self.__str__()