nome = input()
ec = int(input())
nome = nome.strip()

if ec == 1:
    casado = input()
    casado = casado.strip()
    letras = len(nome) + len(casado)
    print(letras)

elif ec == 2 :
    solteiro = len(nome)
    print(solteiro)
