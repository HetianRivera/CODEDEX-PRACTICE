Pesos = int(input('What do you have left in pesos? '))
Soles = int(input('What do you have left in soles? '))
Reais = int(input('What do you have left in reais? '))

usd = (Pesos * 0.00027) + (Soles * 0.30) + (Reais * 0.19)

print(usd)