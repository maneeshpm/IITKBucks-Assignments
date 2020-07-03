from flask import Flask, request, jsonify
from threading import Thread
from hashlib import sha256
from queue import Queue

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>\"Rabbit, Fire up the server!\"</h3>Thor,<br>The strongest avenger"

@app.route('/start', methods=['POST'])
def start():

    def mine(data, queue):  
        def hashf(st,nonce):
            st += str(nonce)
            return sha256(st.encode('utf-8')).digest()
    
        target = 0x0000000F00000000000000000000000000000000000000000000000000000000
        maxnonce = 2 ** 32

        for i in range(maxnonce):
            if int.from_bytes(hashf(data, i), 'big') <= target:
                resultNonce.put(i)
                print("NONCE FOUND: {}, HASH: {}".format(i, bytes.hex(hashf(data,i))))
                break
    
    global resultNonce
    resultNonce = Queue()   
    data = request.json['data']
    thread = Thread(target=mine, args=(data,resultNonce,))
    thread.start()
    return "MINING!",200
    

@app.route('/result')
def result():
    try:
        nonce = resultNonce.get(False)
        return jsonify({"result":"found", "nonce":nonce})
    except:
        return jsonify({"result":"searching", "nonce":-1})

if __name__ == '__main__':
    app.run(debug=True, port = 8787)