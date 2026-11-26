"""
Problem Statement
Count how many times each word appears in a customer review. Ignore capital letters.

Example Input
review = "Good product good price Fast delivery GOOD quality fast support"

Expected Output
good : 3
product : 1
price : 1
fast : 2
delivery : 1
quality : 1
support : 1

"""

review = "Good product good price Fast delivery GOOD quality fast support"
words = review.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1 #word_count.get(word, 0) gives the current count, or 0 if the word is new. Adding 1 updates the count.

for word in word_count:
    print(word, ":", word_count[word])
