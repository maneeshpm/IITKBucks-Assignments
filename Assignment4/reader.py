from classes import Txn, Inp, Output
path = input("Enter path of the dat file: ")

txn = Txn()
txn.readTxnFile(path)
txn.getTxnDetails()
   

