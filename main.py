print('привет,тебе доступны следующие функции: \n\tPOST\n\tGET\n\tUPDATE\n\tDETAIL')
from views import get_data, get_one_data, post_data, delete_data, update_data

while True:
    operation = input('введите действие: ')
    if operation == 'GET':
        print(get_data())
    elif operation == 'DETAIL':
        print(get_one_data())
    elif operation == 'POST':
        print(post_data())
    elif operation == 'PUT':
        print(update_data())
    elif operation == 'DELETE':
        print(delete_data())
    else:
        print('нет такого действия')


