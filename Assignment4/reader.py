from classes import Txn, Inp, Output
path = input("Enter path of the dat file: ")

txn = Txn()
with open(path, 'rb') as txnFile:

    txn.noInputs = int.from_bytes(txnFile.read(4), 'big')
    for i in range(txn.noInputs):
        txnID = txnFile.read(32).hex()
        opIndex = int.from_bytes(txnFile.read(4), 'big')
        signLen = int.from_bytes(txnFile.read(4), 'big')
        sign = bytes.fromhex(txnFile.read(signLen).hex())
        inp = Inp(txnID, opIndex, sign)
        txn.totInput.append(inp)

    txn.noOutputs = int.from_bytes(txnFile.read(4), 'big')
    for i in range(txn.noOutputs):
        noCoins = int.from_bytes(txnFile.read(8), 'big')
        lenPubKey = int.from_bytes(txnFile.read(4), 'big')
        pubKey = txnFile.read(lenPubKey)
        op = Output(noCoins, pubKey)
        txn.totOutput.append(op)

txn.getTxnDetails()
   

