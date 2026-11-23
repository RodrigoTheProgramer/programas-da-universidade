# sistema de cadastro de pessoas

pessoas = []


# função para cadastrar uma pessoa
def cadastrar_pessoa(nome, idade, telefone):
    pessoa = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pessoas.append(pessoa)
    return "Pessoa cadastrada com sucesso!"


# função para listar as pessoas
def listar_pessoas():
    if len(pessoas) == 0:
        print("\nNenhuma pessoa cadastrada.")
    else:
        print("\n--- PESSOAS CADASTRADAS ---")

        for pessoa in pessoas:
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Telefone: {pessoa['telefone']}")
            print("------------------------")


# função para pesquisar uma pessoa
def pesquisar_pessoa(nome):
    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome.lower():
            return pessoa

    return None


# função para mostrar a quantidade de cadastros
def quantidade_pessoas():
    return len(pessoas)


# função principal do aplicativo
def menu():
    while True:
        print("\n===== SISTEMA DE CADASTRO =====")
        print("1 - Cadastrar pessoa")
        print("2 - Listar pessoas")
        print("3 - Pesquisar pessoa")
        print("4 - Quantidade de pessoas cadastradas")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n--- NOVO CADASTRO ---")

            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            telefone = input("Digite o telefone: ")

            resultado = cadastrar_pessoa(nome, idade, telefone)
            print(resultado)

        elif opcao == "2":
            listar_pessoas()

        elif opcao == "3":
            nome = input("\nDigite o nome que deseja pesquisar: ")

            resultado = pesquisar_pessoa(nome)

            if resultado:
                print("\nPessoa encontrada!")
                print(f"Nome: {resultado['nome']}")
                print(f"Idade: {resultado['idade']}")
                print(f"Telefone: {resultado['telefone']}")
            else:
                print("\nPessoa não encontrada.")

        elif opcao == "4":
            total = quantidade_pessoas()
            print(f"\nTotal de pessoas cadastradas: {total}")

        elif opcao == "5":
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


# executar o aplicativo
menu()