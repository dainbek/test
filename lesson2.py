#  CRUD интернет магазина на функциях.работа с json

    # c - create
    # r - read
    # u - update
    # d - delete

# JSON(javascript object notation) - 
# простой формат обменна данными.

# import json
# data = {
#     'name': 'john',
#     'age' : 30,
#     'last_name': None,
#     'is_admin' : False
# } 

# json_obj = json.dumps(data) # сериализация(переводим данные в json )
# print(json_obj)


# python_obj = json.loads(json_obj)# десериализация
# #(переводим с json в python)
# print(python_obj)


# РАЗНИЦА ТИПОВ ДАННЫХ
# PYTHON        JSON
# dict          object
# list          array
# # tuple         arrray
# str             string
# int             number
# float           number
# True ,false     true,false
# none            null


# import json
# with open('test.json') as file:
#     # print(file.read())
#     # print(file)
#     print(json.dumps(file.read()))


# import json

# data = {'is_admin': True}
# print(json.dumps(data))

# with open('test.json') as file:
#     print(json.dump(file))

#разница между loadsи loads,а также dump  и dumps в том,
# что loads/dump - принимают сам файл, 
# dumps/loads- принимают строку