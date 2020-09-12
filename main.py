import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients #Permite tener acceso a la variable global client, caso contrario no funciona

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('Client isn\'t in client list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client isn\'t in client list')


def search_client(client_name):
    global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def list_clients():
    global clients
    print('uid | name | company | email | position')
    print('*'*50)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'],
        ))
        #print('{}: {}'.format(idx, client['name']))


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[L]ist client')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))
        if field == 'exit':
            field = None
            break
    if not field:
        sys.exit()

    return field


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')
        
        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()

    return client_name 


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else: 
            print('The client: {} isn\'t in the client\'s list'.format(client_name))
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

    _save_clients_to_storage()