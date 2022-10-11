from Aviao import Aviao

deque = Aviao()

deque.adcAviao("Boeing 274", "Boeing", "RJ", "Japão", "10", 1)
deque.adcAviao("Douglas DC-3", "Douglas Aircraft Company", "SP", "EUA", "21", 2)

def menu():
    print("")
    print("*----Bem vindo(a) ao sistema!----*")
    print("")
    print("       __|__       ")
    print("--o--o--(_)--o--o--")
    print("")
    print("Opções de ação:")
    print("1 - Adicionar voo na fila de decolagem")
    print("2 - Listar aviões aguardando na fila de decolagem")
    print("3 - Mostrar qual o proximo avião a decolar")
    print("4 - Buscar avião")
    print("5 - Decolar proximo avião da lista")
    print("6 - Total de aviões na fila de decolagem")
    print("")

    codigo = int(input("Digite a opção que deseja: "))

    if codigo == 1:

        modelo = input("Digite o modelo do avião: ")
        empresa = input("Digite a empresa do avião: ")
        origem = input("Qual o local de origem? ")
        destino = input("Qual o destino? ")
        numPassageiros = input("Qual o numero de passageiros? ")
        numVoo = int(input("Digite o numero do voo: "))
        deque.adcAviao(modelo, empresa, origem, destino, numPassageiros, numVoo)
        print("")
        print("Voo adicionado com sucesso!")
        menu()

    elif codigo == 2:
        
        if deque.vazio():
            print("")
            print("Nenhum avião na fila de decolagem")
            print("")
            menu()
        else:
            print("")
            print("Aviões na fila de decolagem: ")
            print("")

            for aviao in deque.avioes:
                print("----------------------")
                print("Modelo: " + aviao[0])
                print("Empresa: " + aviao[1])
                print("Origem: " + aviao[2])
                print("Destino: " + aviao[3])
                print("Passageiros: " + aviao[4])
                print("Numero do voo: " + str(aviao[5]))

            print("----------------------")
            print("")
            menu()

    elif codigo == 3:
        
        if deque.vazio():
            print("")
            print("Nenhum avião na fila de decolagem")
            print("")
            menu()
        else:
            print("")
            print("Proximo avião a decolar: ")
            print("----------------------")
            print("Modelo: " + deque.avioes[0][0])
            print("Empresa: " + deque.avioes[0][1])
            print("Origem: " + deque.avioes[0][2])
            print("Destino: " + deque.avioes[0][3])
            print("Passageiros: " + deque.avioes[0][4])
            print("Numero do voo: " + str(deque.avioes[0][5]))
            print("")
            menu()

    elif codigo == 4:

        print("")
        num = int(input("Digite o numero do voo: "))
        print("")

        avioes = deque.avioes

        for aviao in avioes:
            if aviao[5] == num:
                modelo = aviao[0]
                empresa = aviao[1]
                origem = aviao[2]
                destino = aviao[3]
                numPassageiros = aviao[4]
                numVoo = aviao[5]
                print("Modelo: " + modelo)
                print("Empresa: " + empresa)
                print("Origem: " + origem)
                print("Destino: " + destino)
                print("Passageiros: " + numPassageiros)
                print("Numero do voo: " + str(numVoo))
        print("")
        menu()

    elif codigo == 5:
        deque.decolar()
        print("")
        print("Avião decolado com sucesso!")
        print("")
        menu()

    elif codigo == 6:
        total = deque.tamanho()
        if total > 0:
            print("")
            print("Total de aviões na fila de decolagem: " + str(total))
            print("")
            menu()
        else:
            print("")
            print("Nenhum avião na fila de decolagem")
            print("")
            menu()

menu()