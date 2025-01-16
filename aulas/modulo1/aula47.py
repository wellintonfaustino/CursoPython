"""
  Faça um jogo para o usuário adivinhar a palavra secreta
  - O usuario deverá digitar apenas uma letra
  - Ao digitar uma letra, o programa irá verificar se ela está presente na palavra secreta
  - Se a letra estiver presente, o programa irá mostrar as posições em que ela está presente na palavra secreta
  - Caso o usuario digite uma letra que não estiver presente na palavra secreta, o programa irá mostrar que ela não estiver presente na palavra secreta
  - O jogo termina quando o usuario acerta a palavra secreta ou quando o número de tentativas é esgotado
  - Mostre a quantidade de tentativas
"""



tentativas = 0
palavra_secreta = 'secreta'
palavra_secreta_mostrada = '*' * len(palavra_secreta)

while palavra_secreta != palavra_secreta_mostrada:
  tentativas += 1

  print('A palavra secreta é:')
  print(palavra_secreta_mostrada)
  print(f'Tentativa {tentativas}: Informe uma letra')
  letra = input()

  # Substitui os * pela letra acertada
  for i in range(len(palavra_secreta)):
    if palavra_secreta[i] == letra:
      palavra_secreta_mostrada = palavra_secreta_mostrada[:i] + letra + palavra_secreta_mostrada[i+1:]

  if palavra_secreta_mostrada == palavra_secreta:
    print(f'Parabéns, vocé acertou a palavra {palavra_secreta} em {tentativas} tentativas!')