import hashlib

class Inp:
    def __init__(self, txnID, opIndex, sign):
        self.txnID = txnID
        self.opIndex = opIndex
        self.sign = sign
        self.lenSign = len(self.sign)

    def getBinaryInput(self):
        return ((bytes.fromhex(self.txnID))
        +(self.opIndex.to_bytes(2, byteorder = 'big'))
        +(self.lenSign.to_bytes(4, byteorder = 'big'))
        +(self.sign))

class Output:
    def __init__(self, noCoins, pubKey):
        self.noCoins = noCoins
        self.pubKey = pubKey
        self. lenPubKey = len(self.pubKey)

    def getBinaryOutput(self):
        return (self.noCoins.to_bytes(8, byteorder = 'big')
        +self.lenPubKey.to_bytes(4,byteorder = 'big')
        +self.pubKey)

class Txn:
    totInput=[]
    totOutput=[]
    def _init_(self):
        self.noInputs = 0
        self.noOutputs = 0
        self.totInput = []
        self.totOutput = []

    def getTxnData(self):
        data = self.noInputs.to_bytes(4, byteorder = 'big')
        for inps in self.totInput:
            data += inps.getBinaryInput()
        data += (self.noOutputs.to_bytes(4, byteorder = 'big'))
        for ops in self.totOutput:
            data += (ops.getBinaryOutput())
        return data

    def getTxnHash(self):
        h = hashlib.sha256()
        h.update(self.getTxnData())
        return h.hexdigest()

txn = Txn()

noInputs = int(input("Enter the number of inputs: "))
txn.noInputs = noInputs
for x in range(txn.noInputs):
    print("==================== Input #{} ====================".format(x))
    txnID = input("Enter Transaction id: ")
    opIndex = int(input("Enter index of output: "))
    sign = bytes.fromhex(input("Enter the signature: "))
    inp = Inp(txnID, opIndex, sign)
    txn.totInput.append(inp)

print()
noOutputs = int(input("Enter the number of outputs: "))
txn.noOutputs = noOutputs
for x in range(txn.noOutputs):
    print("===================== Output #{} =======================".format(x))
    noCoins = int(input("Enter the number of coins: "))
    keyPath = input("Enter the path of the key: ")
    k = open(keyPath, 'r')
    pubKey = (k.read()).encode('utf-8')
    op = Output(noCoins, pubKey)
    txn.totOutput.append(op)
    
file = open(str(txn.getTxnHash())+".dat", 'w')
file.write(str(txn.getTxnData()))
file.close()
print("\n{} created successfully!".format(str(txn.getTxnHash())+".dat"))

    