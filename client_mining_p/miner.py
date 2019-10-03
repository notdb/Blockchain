import hashlib
import requests
import json
import sys
import uuid
from pathlib import Path
## Find a way to request the last_block from the server using the requests library
# TODO: Implement functionality to search for a proof 
def proof_of_work(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    proof = 0
    while valid_proof(block_string, proof) is False:
        proof += 1

    return proof

def valid_proof(block_string, proof):
    guess = f'{block_string}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://127.0.0.1:5000"

    coins_mined = 0
    # Run forever until interrupted
    ## Make a UUID, strip - from string
    config = Path('my_id.txt')
    contents = ''
    if config.is_file() is True:
        f = open("my_id.txt", "r")
        contents = f.read()
        f.close()
        print(contents)
    else:
        testString = uuid.uuid1()
        testString2 = str(testString)
        testString3 = testString2.replace('-', '')
        f = open("my_id.txt", 'w+')
        f.write(testString3)
        f.close()
        f = open("my_id.txt", "r")
        contents = f.read()
        print(f"{contents} this is a written version")
    while True:
        response = requests.get('http://127.0.0.1:5000/last_block')
        block = response.json()
        block['id'] = contents
        proof = {}
        proof['proof'] = proof_of_work(block['last-block'])
        proof['id'] = contents
        sendblock = requests.post('http://127.0.0.1:5000/mine', json=proof)
        coins_mined += 1
        #print(sendblock.json(), coins_mined)
