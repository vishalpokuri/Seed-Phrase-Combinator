from itertools import permutations

# List of words
words = ["ALLEY", "ACROSS", "AVERAGE", "FEDERAL", "FOUND", "FRIEND", "FROST", "GUITAR", "HOLD", "INPUT"]

# Known words
first_word = "ART"
sixth_word = "TAPE"

# Generate permutations
perms = permutations(words)

# Write permutations to a file
with open("seed_phrases.txt", "w") as f:
    for perm in perms:
        # Construct the seed phrase
        seed_phrase = [first_word] + list(perm[:4]) + [sixth_word] + list(perm[4:])
        f.write(' '.join(seed_phrase).lower() + "\n")
