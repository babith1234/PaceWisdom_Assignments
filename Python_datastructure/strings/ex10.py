input_sequence = input("Enter the comma seperated words")
words = input_sequence.split(",")
unique_words=set(words)
sorted_letters = sorted(unique_words)

print(sorted_letters)