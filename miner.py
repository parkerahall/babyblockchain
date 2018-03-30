import hashlib, socket, sys
import blockchain_messages_pb2 as pc

MSG_SIZE = 512

def hash_func(inp):
	return hashlib.sha256(inp).hexdigest()

class MiningSocket:
	def __init__(self, ip, port):
		self.socket = socket.socket()
		self.ip = ip
		self.port = port

	def mine(self):
		self.socket.connect((self.ip, self.port))
		message_bytes = self.socket.recv(MSG_SIZE)
		
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
					if test_hash[:num_zeros] == prefix:
						break
					nonce += 1

				self.socket.send(str(nonce))
				message_bytes = self.socket.recv(MSG_SIZE)
		except:
			self.socket.close()

if __name__ == "__main__":
	mine_port = 1203
	if len(sys.argv) == 2:
		mine_port = int(sys.argv[1]) * 1200 + 3
	ms = MiningSocket('localhost', mine_port)
	ms.mine()