# Preenchimento de Vetor I

#Desafio
#Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

#Entrada
#A entrada contém um valor inteiro (V<=50).

#Saída
#Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.

N=[0,0,0,0,0,0,0,0,0,0]
v= int(input())

for i in range(len(N)):
    N[i] = v
    v = v*2
    print('N[{}] = {}'.format(i,N[i]))
