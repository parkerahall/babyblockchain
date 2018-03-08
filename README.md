# babyblockchain
Basic implementation of blockchain in python.

System is composed of:
    - baby_blockchain.py => primary location of chain, serves all clients
    - client.py => creates new client thread to add elements to blockchain and store block hashes
    - miner.py => creates new mining thread to perform proof-of-work to add block to chain