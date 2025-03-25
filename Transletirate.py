from ParameterNames import array_to_find


def transliterate(words: list[str]):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'i', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya', " ": " ", "/": "_"
    }

    result = []
    for word in words:
        translated_text = ""
        for index in range(len(word)):
            if word[index].lower() in translit_dict:
                translated_text += translit_dict[word[index].lower()]
            else:
                translated_text += word[index]
        translated_text = translated_text.title()
        result.append(translated_text.replace(' ', ''))
    return result


translated_words = transliterate(array_to_find)
with open('ResultNames.txt', 'w', encoding='UTF-8') as result_file:
    maxLength = len(max(translated_words, key=len))
    [print(f"{i + " " * (maxLength - len(i))}", file=result_file) for i in translated_words]
