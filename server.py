import hashlib, socket, threading, sys
import blockchain_messages_pb2 as pc
import baby_blockchain as bbc

MSG_SIZE = 512

class ServeThread(threading.Thread):
	def __init__(self, serve, sock, ci):
		super(ServeThread, self).__init__()
		self.server = serve
		self.socket = sock
		self.client_id = ci

	def run(self):
		data = self.socket.recv(MSG_SIZE)
		while data != '\n' and data != '':
			self.server.add_data(data, self.client_id)
			data = self.socket.recv(MSG_SIZE)

class Server:
	def __init__(self, chain, connect, update, verify, mine, diff):
		self.chain          =   chain
		self.connect_port   =   connect
		self.update_port    =   update
		self.verify_port    =   verify
		self.mine_port      =   mine

		self.miner          =   self.init_miner()
		self.difficulty      =   diff
		self.client_list    =   []

		self.lock           =   threading.Lock()

	def init_miner(self):
		mine_server = socket.socket()
		mine_server.bind(('localhost', self.mine_port))
		mine_server.listen(1)

		miner, addr = mine_server.accept()
		ip, port = addr
		print("MINER AT " + ip + ": " + str(port))

		return miner

	def add_data(self, data, ci):
		self.lock.acquire()
		
		proto_entry = pc.Entry()
		proto_entry.ParseFromString(data)
		entry = bbc.Entry.init_from_proto(proto_entry)
		self.chain.add_data(entry)
		print(self.chain)

		update_message = pc.UpdateMessage()
		update_message.type = pc.UpdateMessage.ENTRY
		update_message.entry.MergeFrom(proto_entry)
		update_bytes = update_message.SerializeToString()
		
		self.update_clients(update_bytes, skip=ci)
		
		if self.chain.is_full():
			check_hash = self.chain.hash()
			is_valid = self.confirm_hash(check_hash)
			print(is_valid)
			if is_valid:
				new_hash = self.mine()
				self.chain.add_new_block(new_hash)

				block_message = pc.UpdateMessage()
				block_message.type = pc.UpdateMessage.BLOCK
				block_message.block.prev_hash = new_hash
				block_message_bytes = block_message.SerializeToString()

				self.update_clients(block_message_bytes)
			else:
				self.chain.replace_last_block()

				self.update_clients("REVERT")
		self.lock.release()

	def update_clients(self, data, skip=-1):
		new_client_list = []
		for client in self.client_list:
			keep_client = True
			if client["id"] != skip:
				try:
					client["update"].send(data)
				except:
					print("CLIENT: " + str(client["id"]) + " HAS DISCONNECTED")
					keep_client = False
			if keep_client:
				new_client_list.append(client)
		self.client_list = new_client_list

	def confirm_hash(self, h):
		total = len(self.client_list)
		verified = 0
		for client in self.client_list:
			client["verify"].send("VERIFY")
			hash_check = client["verify"].recv(MSG_SIZE)
			if hash_check == h:
				verified += 1
		return verified == total

	def mine(self):
		prefix = '0' * self.difficulty
		last_hash = self.chain.last_block_hash()

		mine_message = pc.MineMessage()
		mine_message.hash = last_hash
		mine_message.difficulty = self.difficulty
		mine_bytes = mine_message.SerializeToString()

		self.miner.send(mine_bytes)

		while True:
			nonce = self.miner.recv(MSG_SIZE)

			test_hash = hash_func(last_hash + nonce)
			if test_hash[:self.difficulty] == prefix:
				return test_hash

	def send_connect_message(self, client):
		connect_message = pc.ConnectMessage()
		connect_message.update = self.update_port
		connect_message.verify = self.verify_port

		proto_chain = self.chain.to_proto()
		connect_message.chain.MergeFrom(proto_chain)

		connect_bytes = connect_message.SerializeToString()

		client.send(connect_bytes)
		return client.recv(MSG_SIZE) == "SUCCESS"

	def serve(self):
		connect_server = socket.socket()
		connect_server.bind(('localhost', self.connect_port))
		connect_server.listen(1)

		update_server = socket.socket()
		update_server.bind(('localhost', self.update_port))
		update_server.listen(1)

		verify_server = socket.socket()
		verify_server.bind(('localhost', self.verify_port))
		verify_server.listen(1)

		client_id = 0

		try:
			while True:
				client, addr = connect_server.accept()
				ip, port = addr

				is_connected = self.send_connect_message(client)
				if is_connected:
					print("CONNECTION MADE AT " + ip + ": " + str(port))

					verifier, _ = verify_server.accept()
					updater, _ = update_server.accept()
					client_dict = {"verify": verifier, "update": updater, "id": client_id}
					self.client_list.append(client_dict)
					
					st = ServeThread(self, updater, client_id)
					st.start()

					client_id += 1
		finally:
			connect_server.close()
			update_server.close()
			verify_server.close()
			print("\nGOODBYE")

def hash_func(inp):
	return hashlib.sha256(inp).hexdigest()

if __name__ == "__main__":
	connect_port = 1200
	update_port = 1201
	verify_port = 1202
	mine_port = 1203
	if len(sys.argv) == 2:
		connect_port = int(sys.argv[1]) * 1200
		update_port = connect_port + 1
		verify_port = update_port + 1
		mine_port = verify_port + 1
	if len(sys.argv) == 5:
		connect_port = int(sys.argv[1])
		update_port = int(sys.argv[2])
		verify_port = int(sys.argv[3])
		mine_port = int(sys.argv[4])
	c = bbc.Chain([], 3, hash_func)
	s = Server(c, connect_port, update_port, verify_port, mine_port, 2)
	s.serve()



