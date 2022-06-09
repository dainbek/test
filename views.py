import json
import random

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def get_one_data():
    data = get_data()
    id = int(input('введите id продукта: '))
    element = list(filter(lambda x: x['id'] == id ,data))
    return element[0]

def post_data():
    data = get_data()
    data.append({
        "id": random.randint(1, 10000000000),
        "name": input('введите название продукта: '),
        "price": float(input('введите цену на продукта: '))
    })    
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'CREATED'



def update_data():
    data = get_data()
    id = int(input('введите id продукта: '))
    update = list(filter(lambda x : x['id']== id ,data))
    # update = false
    #update = ['asdas']
    if not update:
        index = data.index(update[0])
        data[index]['name'] = input('введите новое название: ')
        data[index]['price'] = float(input('введите новую цену: '))

        with open(FILE_PATH, 'w') as file:
           json.dump(data,file)
        return 'UPDATED'

def delete_data():
    data = get_data()
    id = int(input('введите id: '))
    delete = list(filter(lambda x : x['id']==id,data))

    if not delete:
        return 'нет такого продукта!'

    index = data.index(delete[0])
    data.pop(index)

    json.dump(data, open(FILE_PATH, 'w'))

    return 'DELETED'
delete_data()

