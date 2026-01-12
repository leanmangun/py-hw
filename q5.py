words = ["This", "is", "good", "is"]

freq = {}
for word in words:
    lower_word = word.lower()  # Create a new variable
    if lower_word in freq:
        freq[lower_word] += 1
    else:
        freq[lower_word] = 1

print(freq)