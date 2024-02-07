from coincurve import PublicKey, PrivateKey
from bip44 import Wallet
from bip44.utils import get_eth_addr

def generate_eth_address_from_seed_phrase(seed_phrase):
    w = Wallet(seed_phrase)
    _, pk = w.derive_account("eth", account=0)
    return get_eth_addr(pk)

def main():
    # Read your public key
    known_public_key = "0xYourKey"
    i=0
    # Read seed phrases from file
    with open("seed_phrases.txt", "r") as f:
        seed_phrases = f.read().splitlines()

    # Iterate through each seed phrase
    for seed_phrase in seed_phrases:
        # Generate Ethereum wallet public key for the current seed phrase
        eth_public_key = generate_eth_address_from_seed_phrase(seed_phrase)
        print("checking seed "+str(i))
        i=i+1

        # Check if the generated public key matches the known public key
        if eth_public_key == known_public_key:
            print("Matching Seed Phrase:", seed_phrase)
            break
    else:
        print("No matching seed phrase found for the provided public key.")

if __name__ == "__main__":
    main()
