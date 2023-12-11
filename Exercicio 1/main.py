import os
import json

if not os.path.exists('config.json'):
    with open('config.json', 'w') as file:
        json.dump({}, file)

option = input("Escolha uma opção:\n1 - Read configuration\n2 - Write configuration\n")

if option == '1':
    with open('config.json', 'r') as file:
        data = json.load(file)
        if data:
            print(data)
        else:
            print("O arquivo não contém informações.")
elif option == '2':
    server_name = input("Informe o nome do servidor: ")
    server_ip = input("Informe o IP do servidor: ")
    server_password = input("Informe a senha do servidor: ")

    data = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    with open('config.json', 'w') as file:
        json.dump(data, file)

    print("Informações salvas com sucesso.")
    print(data)
else:
    print("Opção inválida.")