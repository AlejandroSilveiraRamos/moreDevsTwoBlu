from time import sleep

lista_notas = []
lista_historico = []

nome = str(input('Digite seu nome: '))
sobreNome = str(input('Digite seu sobrenome: '))
idade = int(input('Digite sua idade: '))

situacao = 'Reprovado'

while situacao == 'Reprovado':
    for lista in range(0, 2):
        nota = int(input('Digite sua nota: '))
        lista_notas.append(nota)
    
    media = sum(lista_notas) / len(lista_notas)

    if media >= 7:
        sleep(2)
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    dicionario = {'Nome': nome, 'Sobrenome': sobreNome, 'Idade': idade}
    print(f'Suas notas são {lista_notas} e sua média é {media}, Você está {situacao}')
    if situacao == 'Reprovado':
        lista_historico.append(lista_notas)

    lista_notas = []
    
print('Saiu', lista_historico)
