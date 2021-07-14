# Triangulo

#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


#Perimetro = XX.X


#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


#Area = XX.X

#Entrada
#A entrada contém três valores reais.

#Saída
#O resultado deve ser apresentado com uma casa decimal.

a = [float(x) for x in input().split()]
#complete o desafio
if (((a[0] + a[1]) > a[2]) and ((a[1] + a[2]) > a[0]) and ((a[0] + a[2]) > a[1])):
  p = sum(a)
  print(f'Perimetro = %.1f' % p)
else:
  area = ((a[0] + a[1])*a[2])/2.0
  print(f'Area = %.1f' % area)
