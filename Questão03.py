#Questão 3 Lista 2
n1 = int(input('Digite sua 1ª nota: '))
n2 = int(input('Digite sua 2° nota: '))
n3 = int(input('Digite sua 3ª nota: '))
nota = (n1 + n2 + n3) / 3
if nota >= 7 and nota < 10:
    print ('Aprovado!!')
elif nota >= 4 and nota < 7:
    print ('Prova Final!')
else:
    print ('Reprovado!')



