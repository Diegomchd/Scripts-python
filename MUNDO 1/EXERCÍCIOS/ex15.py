km = float(input('Quantos quilômetros você percorreu? '))
dias = int(input('Quantos dias você ficou com o carro? '))
preco = (km * 0.15) + (dias * 60)
print(f'O preço a ser pago é de R$ {preco:.2f}')
