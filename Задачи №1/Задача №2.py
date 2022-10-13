def number_of_vowels(text):
    vowelsCount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for textChar in text :
        textChar = str.lower(textChar)
        if(textChar in vowels): vowelsCount+=1

    return vowelsCount


#
print(number_of_vowels("") == 0)
print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)