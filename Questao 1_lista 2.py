contador_regular = 0
contador_bom = 0
contador_otimo = 0
for i in range (3)
opiniao = int(input('Digite sua opinião sobre o filme:'))
    if opiniao == 1:
       contador_regular = contador_regular + 1
        print('Regular')
    elif opiniao == 2:
         contador_bom = contador_bom + 1
         print('bom')
    else: opiniao == 3:
        contador_otimo = contador_otimo + 1
        print('Otimo')
print('Qtd de opiniao em REGULAR =%d' % contador_regular)
print('Qtd de opiniao em BOM =%d' % contador_bom)
print('Qtd de opiniao em ÓTIMO =%d' % contador_otimo)
