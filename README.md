# Seed-Phrase-Combinator

Simple Python [bip44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) implementation. [Mnemonic](https://github.com/trezor/python-mnemonic) + [bip32](https://github.com/darosior/python-bip32).

## Install

`pip install bip44`

seed_phrase_type-1.py is for generating seed-phrase combinations and Publickeyfinder is for finding a Secret Phrase if a Public Key associated with a seed phrase is matching the given seed phrase. 

findoutlast2.py is for finding seed phrases if you have 10 words and permutating by taking 2 words from a list of 2048 words (bip39_wordlist)
