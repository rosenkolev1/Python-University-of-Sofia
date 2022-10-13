def number_of_vowels(text):
    vowelsCount = 0
    for textChar in text :
        textChar = str.lower(textChar)
        if(textChar == 'a' or textChar == 'e' or textChar == 'i' or textChar == 'o' or textChar == 'u'): vowelsCount+=1
    return vowelsCount


#a, e, i, o, u

print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)