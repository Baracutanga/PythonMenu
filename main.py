escolha = 0

while (escolha != 7):
    print("Escolha a opção:\n")
    print("1. Criar Turma")
    print("2. Adicionar Professor")
    print("3. Adicionar Estudante")
    print("4. Adicionar Nota")
    print("5. Consultar Nota")
    print("6. Salvar Nota")
    print("7. Sair")

    escolha = int(input("> "))

    if escolha == 1:
        print("Turma criada!")
        input("Pressione Enter para continuar...")
    elif escolha == 2:
        print("Professor adicionado!")
        input("Pressione Enter para continuar...")
    elif escolha == 3:
        print("Estudante adicionado")
        input("Pressione Enter para continuar...")
    elif escolha == 4:
        print("Nota adicionada!")
        input("Pressione Enter para continuar...")
    elif escolha == 5:
        print("Consulta de Nota: ")
        input("Pressione Enter para continuar...")
    elif escolha == 6:
        print("Nota salva!")
        input("Pressione Enter para continuar...")
    elif escolha == 7:
        print("Você saiu.")
        break
    else:
        print("Número inválido!!")
