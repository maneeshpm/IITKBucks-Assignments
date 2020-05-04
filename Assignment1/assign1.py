import hashlib

def hashf(st, nonce):
    h = hashlib.sha256()
    st += str(nonce)
    h.update(st.encode('utf-8'))
    return h.hexdigest()

target = 0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
maxnonce = 2 ** 32
s = input()

for i in range(maxnonce):
    if int(hashf(s,i),16) <= target:
        print(i)
        # print(hashf(s,i))
        break   


