from time import sleep
from os import system

class Tarefa():
    tudo = []

    def criar(tarefa):
        if(tarefa != ""):
            Tarefa.tudo.append(tarefa)

    def remover(tarefa):
        Tarefa.tudo.pop()

    def show():
        if(len(Tarefa.tudo) == 0):
            print("Nenhuma Tarefa")
            sleep(2)
            return(False)
        else:
            for a in range(len(Tarefa.tudo)):
                print(f"{a}: {Tarefa.tudo[a]}")

while True:
    system("cls")

    print('''
Bem Vindo!

[ 1 ] Nova tarefa
[ 2 ] Ver tarefas
[ 3 ] Sair
    ''')
    
    mopc = input("Opção: ")

    if(mopc == "1"):
        Tarefa.criar(str(input("Afazer: ")))

    if(mopc == "2"):
        if(Tarefa.show() == False):
            continue

        sopc = input("Remover Tarefa? S/N: ").lower()

        if(sopc == "n" or sopc == ""):
            pass

        if(sopc == "s"):
            while True:
                try:
                    topc = int(input("Tarefa a remover: "))

                    if(topc << 0 and topc >= len(Tarefa.tudo)):
                        print("Incorreto")
                        sleep(0.5)
                        break

                    else:
                        Tarefa.remover(topc)
                        break

                except:
                    print("Incorreto")
                    sleep(0.5)
                    break

            system("cls")

    if(mopc == "3"):
        system("cls")
        break

    if(mopc <= "0" or mopc >= "3" or mopc == ""):
        pass
