from itertools import permutations

# Load 2048 words from a file
with open("bip39.txt", "r") as word_file:
    all_words = [word.strip() for word in word_file.readlines()]

# Known words
known_words = ["ozone", "blast", "link", "bundle", "consider", "rain", "what", "sibling", "x", "y"]

# Generate permutations of 2 words from the list
word_permutations = permutations(all_words, 2)

# Write permutations to a file
with open("seed_phrases.txt", "w") as f:
    for permutation in word_permutations:
        # Create a copy of known_words
        seed_phrase = known_words.copy()
        # Append the permutations
        seed_phrase.append(permutation[0])
        seed_phrase.append(permutation[1])
        # Write the seed phrase to file
        f.write(' '.join(seed_phrase) + "\n")
