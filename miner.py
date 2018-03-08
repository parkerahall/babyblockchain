import hashlib, socket, sys

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
		message = self.socket.recv(MSG_SIZE)
		
		try:
			while True:
				bang_index = message.find('!')

				num_zeros = int(message[:bang_index])
				last_hash = message[bang_index + 1:]

				prefix = '0' * num_zeros

				nonce = 0
				while True:
					test_hash = hash_func(last_hash + str(nonce))
					if test_hash[:num_zeros] == prefix:
						break
					nonce += 1

				self.socket.send(str(nonce))
				message = self.socket.recv(MSG_SIZE)
		except:
			self.socket.close()

if __name__ == "__main__":
	mine_port = 1202
	if len(sys.argv) == 2:
		mine_port = int(sys.argv[1])
	ms = MiningSocket('localhost', mine_port)
	ms.mine()