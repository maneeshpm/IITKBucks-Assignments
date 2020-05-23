from block import block


index = int(input("Enter the Index: "))
parentHash = bytes.fromhex(input("Enter parent hash: "))
target = int(input("Enter target: "),16)
path = input("Enter path of body file: ")
body = None
with open(path, 'rb') as f:
    body = f.read()

block = block(index,parentHash,body,target)
