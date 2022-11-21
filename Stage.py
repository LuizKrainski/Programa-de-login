def log_in():
    username = input("Por favor insira seu nome de usuário : ")
    password = input("Por favor insira sua senha : ")

    with open('test_file.txt', 'r') as file:
        for line in file:
            if line == 'Usuario:{0}, Senha:{1}'.format(username, password):
                print ("Saudações," , username, "Agora você está logado")
                return True, username, password
    print (" Desculpe, nome de usuário e senha incorretos, digite novamente para validação ")
    return False, '', ''

def new_user():
    succes = False
    while not succes:
        new_user = input("Por favor, digite seu novo nome de usuário : ")
        new_pass = input("Por favor, digite sua nova senha : ")

        exists = False
        with open("test_file.txt","r") as file:
            for line in file:
                if line.split(',')[0] == 'Usuario:'+new_user:
                    print ('Nome de usuário Inválido: {0} já existe'.format(new_user))
                    exists = True

        if not exists:
            with open("test_file.txt","a") as file:
                file.write('Usuario:{0}, Senha:{1}'.format(new_user, new_pass))
            succes = True
    print ('Você criou um novo usuário com nome de usuário:{0} e senha:{1}'.format(new_user, new_pass))

def main():
    command = username = password = ''
    logged_in = False
    while command != 'Fechar':
        command = input('Escreva o comando: ')
        if command == 'Conecte-se':
            logged_in, username, passowrd = log_in()
        if command == 'Sair':
            logged_in = False
            username = passowrd = ''
        if command == 'Novo usuario':
            if not logged_in:
                new_user()
            else:
                print ('Primeiro logout para criar um novo usuário')

main()
