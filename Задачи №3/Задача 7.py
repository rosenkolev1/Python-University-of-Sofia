def translator_to_shlokavica(text):
    shlokavica_alphabet = ["A", "B", "V", "G", "D", "E", "J", "Z", "I", "Y", "K", "L", "M", "N", "O", "P", "R", "S", 
    "T", "U", "F", "H", "C", "4", "6", "6T", "U", "Y", "YU", "Q"]

    normal_cyrilic_alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", 
    "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ь", "Ю", "Я"]

    alphabet_kvpairs = dict(zip(normal_cyrilic_alphabet, shlokavica_alphabet))
    return ''.join([alphabet_kvpairs[symbol] if symbol in alphabet_kvpairs.keys() else symbol for symbol in text])

print(translator_to_shlokavica("""ТОЗИ ТЕКСТ Е МНОГО ГОТИН И АЗ ЛИЧНО МНОГО ГО ХАРЕСВАМ И ОБОЖАВАМ ЪГЛОВО ЮТИИ И 
СТАРИ ЕЛЕМЕНТИ НА УРНИ ЯГОДИ ДРЕСИНГ ЖУРНАЛИСТИКА ЙОДА ШАНТАЖ ИЛИ ЩАНД БЕТИ ПРЕКРАСНА СИ---"""))