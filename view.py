from controller import ControllerCadastro, ControllerLogin
while True:
    print("=========== [MENU] ==========")
    decide = int(input("Digite 1 para cadastrar\nDigite 2 para logar\nDigite 3 para sair\n"))

    if decide == 1:
        nome = input("Digite seu nome: \n")
        email = input("Digite seu email: \n")
        senha = input("Digite sua senha: \n")
        resultado = ControllerCadastro.cadastro(nome, email, senha)

        if resultado == 2:
            print("Nome inválido! ")
        elif resultado == 3:
            print("Email inválido!")
        elif resultado == 4:
            print("Senha inválida!")
        elif resultado == 5:
            print("Email. já cadastrado!")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadastro realizado com sucesso!")
    elif decide == 2:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        resultado = ControllerLogin.login(email, senha)

        if not resultado:
            print("Email ou Senha inválidos")
        else:
            print(resultado)
    else:
        break