#IMPORTING HASHLIB
import hashlib


class MohammadCoin:
    def __init__(self, previousBlockHash, transactions):
        self.previousBlockHash = previousBlockHash
        self.transactions = transactions

        self.block_data = "-".join(transactions) + "=" + previousBlockHash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

Person1 = "A sends 2 NC to B"
Person2 = "C sends 4.1 NC to B"


firstBlockString = MohammadCoin("MohammadCoin Transaction", [Person1, Person2])

print(firstBlockString.block_data)
print(firstBlockString.block_hash)
