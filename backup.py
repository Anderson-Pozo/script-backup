import requests
from connection import get_database

db = get_database()
url = 'https://admin-6c5a5-default-rtdb.firebaseio.com/'
endpoints = [
    'alimentacion',
    'eventos',
    'gastronomia',
    'hospedaje',
    'sitios',
    'transporte',
    'usuarios'
]


def fetch_data(endpoint_position):
    response = requests.get('{}{}{}'.format(url, endpoints[endpoint_position], '.json'))
    data: dict = response.json()
    return data


def format_data(data):
    registers = []
    for val in data:
        if 'Uid' in data[val]:
            data[val].pop('Uid')
        row = data[val]
        registers.append(row)
    return registers


def execute_backup(option):
    try:
        collection_name = db[endpoints[option]]
        collection_name.drop()
        data = fetch_data(option)
        registers = format_data(data)
        collection_name.insert_many(registers)
        return 'Backup {} exitoso'.format(endpoints[option])
    except Exception as error:
        return 'Error al generar respaldo {}'.format(error)


def execute_masive_backup():
    try:
        for endpoint in endpoints:
            collection_name = db[endpoint]
            collection_name.drop()
            data = fetch_data(endpoints.index(endpoint))
            registers = format_data(data)
            collection_name.insert_many(registers)
        return 'Backup exitoso'
    except Exception as error:
        return 'Error al generar respaldo {}'.format(error)
