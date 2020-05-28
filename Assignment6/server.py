from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

m = {}
peers = []
#peers = ["http://localhost:8786/add","http://localhost:8785/add"]


@app.route('/')
def home():
    return "<h3>\"Rabbit, Fire up the server!\"</h3>Thor,<br>The strongest avenger"


@app.route('/add', methods=['POST'])
def add():
    '''
    Recieve post requests and broadcast them to peers conditionally
    '''
    key = int(request.json['key'])
    value = request.json['value']
    
    if(key not in m):
        m[key]= value
        log = "SET {{{} : \"{}\"}}".format(key,value)    
        for peer in peers:
            req = requests.post(url = peer, json= {"key":key,"value":value})
            log += "\nSENT {{{} : \"{}\"}} TO {}, STATUS = {}, {}".format(key,value,peer,req.status_code,req.reason)
        print(log)
        return log
    else:
        return "IGNORED"


@app.route('/list', methods=['GET'])
def lis():
    '''
    Recieve get request and return the current state of list
    '''
    return jsonify(m)


if __name__ == '__main__':
    app.run(debug = True, port = 8787)
