words = ["apple", "banana", "apple", "orange", "banana", "banana"]

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

duplicates = {word: count for word, count in freq.items() if count > 1}

print("Duplicates:", duplicates)