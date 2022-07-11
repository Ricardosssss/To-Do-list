from os import system
from time import sleep
from termcolor import cprint

tudo = []

def task(do):
    tudo.append(do)

system("clear")

while True:
    cprint('''
 ████████╗ ██████╗     ██████╗  ██████╗     ██╗     ██╗███████╗████████╗
 ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝
    ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║███████╗   ██║   
    ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   
    ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   
    ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝   
    ''', "cyan")

    cprint('''
 [ 1 ] Novo afazer
 [ 2 ] Ver os afazeres
 [ 3 ] Sair
''', "yellow")

    opcmain = input(" Opção: ")

    if opcmain != "1" and opcmain != "2" and opcmain != "3":
        system("clear")

    elif opcmain == "1":
        task(input(" Afazer: "))
        system("clear")

    elif opcmain == "2":
        for a in range(len(tudo)):
            cprint(f" {a}: {tudo[a]}", "green")

        if len(tudo) == 0:
            cprint(" Nenhum afazer", "red")
            sleep(1)
            system("clear")
        else:

            opcrm = str(input(" Remover um afazer? S/N: ")).lower()

            if opcrm != "s" and opcrm != "n":
                system("clear")

            elif opcrm == "s":
                while True:
                    try:
                        afazernum = int(input(" Qual afazer deseja remover: "))

                        if afazernum << 0 and afazernum >= len(tudo):
                            cprint(f" Não existe o afazer {afazernum}, tente novamente!", "yellow")
                            
                        else:
                            tudo.pop(afazernum)
                            system("clear")
                            break
                    except:
                        cprint(" Tente novamente", "red")
                        sleep(0.5)
                        system("clear")
                        break

            elif opcrm == "n":
                system("clear")

    if opcmain == "3":
        cprint(" Até a proxima", "cyan")
        sleep(0.5)
        system("clear")
        break