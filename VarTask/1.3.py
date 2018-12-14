#Вариативная СР
#1.3. Создание программы для считывания данных формата CSV c использованием функционала модуля contextlib.



import csv
#contextlib - модуль содержит вспомогательные функции для поддержки оператора with
from contextlib import contextmanager

@contextmanager
#импортируем contextmanager из contextlib 
#и декорируем нашу функцию file_open с ним. 
#Это позволяет нам вызвать file_open используя оператор "with"
def file_open (file):
    try:
        data = open(file, 'r')
        read = csv.reader(data)
        yield read
    except FileNotFoundError:
        print("Файл не найден.")
        read=[]
        yield read #функция возвращает генератор

 
def file_read(reader):
    for row in reader:
        lst =[]
        for el in row:
          lst.append(el)
        print(lst)

if __name__ == "__main__":
  with file_open ('titanic.csv') as f:
        file_read(f)
