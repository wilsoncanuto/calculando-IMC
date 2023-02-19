altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em Kg: '))

IMC = peso / (altura/100)**2

print(IMC)


if IMC < 18.5:
   print(f'seu IMC e de {IMC}, E é classificado como magreza.procure um médico para orientar sua saúde está em risco')


elif IMC > = 18.5 and IMC < 24.9:
     print(f'seu IMC e de {IMC}, E é classificado como normal')

elif IMC > = 25 and IMC  < 29.9:
     print(f'seu IMC e de {IMC}, E é classificado como sobrespeso. Mas bem leve! não se preocupe!')

elif IMC > = 30 and IMC  < 39.9:
     print(f'seu IMC e de {IMC}, E é classificado como obsesidade.Tem que tomar cuidado pois ainda dar tempo para reverter ')


else:
    print("Pode parar de comer e começar a malhar pois o negocio está feio! Obesidade grave")



# Menor que 18,5       Magreza    0
# Entre 18,5 e 24,9    Normal     0
# Entre 25 e 29,9    Sobrepeso  I
# Entre 30 e 39,9    Obesidade  II
# Maior que 40,0     Obsidade Grave III