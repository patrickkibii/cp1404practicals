"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""


user_input = input("Enter a string: ").lower()

words = user_input.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

longest_word = max(len(word) for word in word_counts)
for word, count in sorted(word_counts.items()):
    print(f"{word:{longest_word}} : {count}")
