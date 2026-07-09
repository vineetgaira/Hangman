
word="VINEET"
print("__ "*len(word))

user=input("\nEnter a word:").upper()

for letter1 in user:
    for letter2 in word:
        if letter1==letter2:
            print("success")