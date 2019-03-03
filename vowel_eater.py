# prompt the user to enter a word:
word = str(input("Tell me a word: "))
# complete the for loop:

new_word = ""

for letter in word:
    vowels = ('a', 'e', 'i', 'o', 'u');
    if letter not in vowels:
        new_word += letter
        
print(new_word)