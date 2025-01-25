sentence = input("Enter a sentence: ")

sentence_1 = ''
for char in sentence:
    if char.isdigit():
        sentence_1 += char
print(sentence_1)