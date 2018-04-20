import hashlib, socket, sys
import blockchain_messages_pb2 as pc

MSG_SIZE = 512

def hash_func(inp):
	return hashlib.sha256(inp).hexdigest()

class MiningSocket:
	def __init__(self, ip, port):
		self.connect_socket = socket.socket()
		self.mine_socket = socket.socket()
		self.ip = ip
		self.connect_port = port

		self.balance = 0

	def connect(self):
		self.connect_socket.connect((self.ip, self.connect_port))
		message_bytes = self.connect_socket.recv(MSG_SIZE)

		connect_message = pc.ConnectMessage()
		connect_message.ParseFromString(message_bytes)

		self.mine_port = connect_message.mine
		self.id = connect_message.miner_id

		self.connect_socket.send("SUCCESS")

	def mine(self):
		self.connect()

		self.mine_socket.connect((self.ip, self.mine_port))
		message_bytes = self.mine_socket.recv(MSG_SIZE)
		
		try:
			while True:
				message = pc.MineMessage()
				message.ParseFromString(message_bytes)

				difficulty = int(message.difficulty)
				last_hash = message.hash

				prefix = '0' * difficulty
				nonce = 0
				while True:
					test_hash = hash_func(last_hash + str(nonce))
					if test_hash[:difficulty] == prefix:
						break
					nonce += 1

				nonce_message = pc.NonceMessage()
				nonce_message.nonce = nonce
				nonce_message.miner_id = self.id

				response_bytes = nonce_message.SerializeToString()

				self.mine_socket.send(response_bytes)
				message_bytes = self.mine_socket.recv(MSG_SIZE)
				if message_bytes[:7] == "SUCCESS":
					print("MINED: " + str(nonce) + ", " + test_hash)
					self.balance += int(message_bytes[7:])
					print(self.balance)
					message_bytes = self.mine_socket.recv(MSG_SIZE)
		finally:
			self.mine_socket.close()

if __name__ == "__main__":
	connect_port = 1201
	if len(sys.argv) == 2:
		connect_port = int(sys.argv[1]) * 1200 + 1
	ms = MiningSocket('localhost', connect_port)
	ms.mine()