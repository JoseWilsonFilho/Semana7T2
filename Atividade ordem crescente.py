# Escreva um programa que leia três números e mostre na tela em ordem crescente.

numero_um  = int(input())
numero_dois = int(input()) 
numero_tres = int(input())

lista_exemplo = [numero_um, numero_dois, numero_tres]
lista_teste = sorted(lista_exemplo)

print(lista_teste[0])
print(lista_teste[1])
print(lista_teste[2])


