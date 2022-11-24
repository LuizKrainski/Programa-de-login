def login():
    usuario = input("Por favor insira seu nome de usuário : ")
    senha = input("Por favor insira sua senha : ")

    with open('test_file.txt', 'r') as file:
        for line in file:
            if line == 'Usuario:{0}, Senha:{1}'.format(usuario, senha):
                print ("Saudações," , usuario, "Agora você está logado")
                return True, usuario, senha
    print (" Desculpe, nome de usuário e senha incorretos, digite novamente para validação ")
    return False, '', ''

def novo_usuario():
    succes = False
    while not succes:
        novo_usuario = input("Por favor, digite seu novo nome de usuário : ")
        nova_senha = input("Por favor, digite sua nova senha : ")

        exists = False
        with open("test_file.txt","r") as file:
            for line in file:
                if line.split(',')[0] == 'Usuario:'+novo_usuario:
                    print ('Nome de usuário Inválido: {0} já existe'.format(novo_usuario))
                    exists = True

        if not exists:
            with open("test_file.txt","a") as file:
                file.write('Usuario:{0}, Senha:{1}'.format(novo_usuario, nova_senha))
            succes = True
    print ('Você criou um novo usuário com nome de usuário:{0} e senha:{1}'.format(novo_usuario, nova_senha))

def main():
    command = usuario = senha = ''
    logged_in = False
    while command != 'Fechar':
        command = input('Escreva o comando: ')
        if command == 'Conecte-se':
            logged_in, usuario, senha = login()
        if command == 'Sair':
            logged_in = False
            usuario = senha = ''
        if command == 'Novo usuario':
            if not logged_in:
                novo_usuario()
            else:
                print ('Primeiro logout para criar um novo usuário')

main()
