import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof
def proof_of_work(self):
        """
        Simple Proof of Work Algorithm
        Find a number p such that hash(last_block_string, p) contains 6 leading
        zeroes

        :return: <int> A valid proof
        """
        block_string = json.dumps(self.last_block, sort_keys=True).encode()
        proof = 0
        while not self.valid_proof(block_string, proof):
            proof += 1

        return proof

    @staticmethod
    def valid_proof(block_string, proof):
        """
        Validates the Proof:  Does hash(last_block_string, proof) contain 6
        leading zeroes?

        :param proof: <string> The proposed proof
        :return: <bool> Return true if the proof is valid, false if it is not
        """
        guess = f'{block_string}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:6] == "000000"


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
