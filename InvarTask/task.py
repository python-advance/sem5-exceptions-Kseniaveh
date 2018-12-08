import json


"""Функция для считывания json- данных из файла"""
def read_func_file(name_file):
    try:
        name = open(name_file, 'r') 
        data = json.loads(name.read()) #json.loads - считывание строки в формате JSON в объект Python
        name.close()
    except FileNotFoundError:
        data='error - file not found'
    return data

"""Cчитывания json- данных с использованием менеджера кнтекстов"""
#with open(read_file, 'r') as f:
    #data = json.loads(f.read())
    #print(data)
    
    
"""Функция для проверки существует ли файл"""
def assert_func_file(name_file):
    try:
        name = open(name_file, 'r') 
        data = json.loads(name.read())
        return True
    except FileNotFoundError:
        return False

"""
Функция вывода значения из json-a в виде таблицы, без использования сторонних библиотек
Также, в Python есть возможность реализации данного этапа задания, с помощью библиотеки PrettyTable
Метод strip() - возвращает копию строки, в которой все символы 
были удалены с начала и конца строки (символом по умолчанию является пробел).
"""
def tableJson(json_list):
    max_lengh = 0
    if len(json_list) > 0:
        for key in json_list[0].keys():
            for el in json_list:
                if type(el[key]) == int:
                    if len(str(el[key])) > max_lengh:
                        max_lengh = len(str(el[key]))
                else:
                    if len(el[key]) > max_lengh:
                        max_lengh = len(str(el[key]))
                        
        headers = ["Имя", "Фамилия", "Возраст" , "Email" ]
        title = '|'
        for head in headers:
            sub = max_lengh - len(head)
            title = title + head + sub*' '
            title = title + '|'   
        print(title)
        
        for key in json_list[0].keys():
            for el in json_list:
                if type(el[key]) == int:
                    diff = max_lengh - len(str(el[key]).strip())
                    el[key] = str(el[key]).strip() + diff*' '
                else:
                    diff = max_lengh - len(el[key])
                    el[key] = el[key].strip() + diff*' '
        input = '|'
        
        for elem in json_list:        
            input = '|'
            for key in json_list[0].keys():                
                input = input + elem[key] + '|'                
            print(input)
                


def call_func():
    read_file = 'new_file.json'
    print(read_func_file(read_file))
    print(assert_func_file(read_file))
    value = read_func_file(read_file)
    tableJson(value["all_participant"])
    assert assert_func_file('new_file.json')== True 
    assert assert_func_file('new_file2.json')== False

if __name__ == "__main__":
    call_func()
