dados = dict()
lista = []

while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = str(input('Sexo [m/f]: '))
    lista.append(dados.copy())
    dados.clear()

    continuar = input(f'continuar (s/n)?: ')
    if continuar == 'n':
        break



##calculo da media e lista das mulhees
somma = 0
mulheres = []
for i in lista:
    somma = somma + i['idade']
    if i['sexo'] == 'f':
        mulheres.append(i.copy())


idade_media = somma/len(lista)

velhos = []
for i in lista:
    if i['idade'] > idade_media:
        velhos.append(i.copy())

print(f'tem {len(lista)} pessoas')
print(f'idade media é {idade_media}')
print(mulheres)
print(velhos)