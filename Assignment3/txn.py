import hashlib

from classes import Txn, Inp, Output

txn = Txn()

noInputs = int(input("Enter the number of inputs: "))
txn.noInputs = noInputs
for x in range(txn.noInputs):
    print("==================== Input #{} ====================".format(x))
    txnID = bytes.fromhex(input("Enter Transaction id: "))
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
    
txn.generateTxnFile()
    