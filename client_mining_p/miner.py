import hashlib
import requests
import json
import sys

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
    return guess_hash[:3] == "000"

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://127.0.0.1:5000"

    coins_mined = 0
    # Run forever until interrupted
   
        # TODO: Get the last proof from the server and look for a new one
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
    #   pass
    response = requests.get('http://127.0.0.1:5000/last_block')
    block = response.json()
    proof = proof_of_work(block['last-block'])
    print(proof)
    coins_mined += 1
    print(proof)
    sendblock = requests.post('http://127.0.0.1:5000/mine', json=proof)
    print(f'{sendblock.url} AAAAA')
    print(f'{sendblock} bbbbbbbbb')
