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