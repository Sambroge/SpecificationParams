from bs4 import BeautifulSoup
from ParameterNames import array_to_find
from SpecificationPath import path

max_len = max(map(len, array_to_find))
#Путь, в функции "open" ниже, нужно поменять на свой. Путь до файла спецификации формата .xml
with open(path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file.read(), features='xml')
    with open('ResultGuids.txt', 'w', encoding='UTF-8') as result_file:
        for i in soup.Parameters.find_all("Parameter"):
            name = i.get("Name")
            id = i.get("ID")
            if name in array_to_find:
                print(f'{name + ' ' * (max_len - len(name))}: {id}', file=result_file)
