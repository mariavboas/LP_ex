# exercicios para a materia de linguagens e programacao

# exercicio 11
def exercicio_1(): #
    while True: # utilizei while para que, caso seja inserido um valor invalido, o codigo reincie
        try: # utilizei o try para iniciar o codigo, ja que podem ocorrer erros durante a execução do programa
            print("1. Escolha dois números interos e um real")
            # pedindo 2 numeros inteiros e um real
            numero_inteiro1 = int(input("Digite o primeiro número inteiro escolhido: "))
            numero_inteiro2 = int(input("Digite o segundo número inteiro escolhido: "))
            numero_real = float(input("Digite o número real escolhido: "))

            # calculando os resultados
            resultado_a = ( 2 * numero_inteiro1) * ( numero_inteiro2 / 2 )
            resultado_b = ( 3 * numero_inteiro1) + numero_real
            resultado_c = numero_real ** 3

            # mostrando os resultados
            print( f'\nO produto do dobro do primeiro número com metade do segundo número é igual a: {resultado_a:.2f}')
            print( f'a soma do triplo do primeiro número com o terceiro número é igual a: {resultado_b:.2f}')
            print( f'O terceiro número elevado ao cubo é igual a: {resultado_c:.2f}')
            break # termina o loop caso nenhum erro tenha sido cometido
        except(ValueError): # roda quando ocorre um erro, e depois reinicia (não há break)
            print("Valor Inválido. Tente Novamente")

# exercicio 12
def exercicio_2():
    while True:
        try:
            altura = float(input("Descubra seu peso ideal! Insira sua altura (em metros): \n")) #pede a altura do usuario
            peso_ideal = (72.7 * altura) - 58
            print(f'O seu peso ideal é: {peso_ideal:.3f}')
            break
        except(ValueError):
            print("Altura inválida. Tente novamente")

# exercicio 13
def exercicio_3():
    while True: # loop para garantir que a altura inserida será valida
        try:
            altura = float(input("\nDescubra seu peso ideal!\nInsira sua altura (em metros): ")) # pede a altura do usuario
            break # reinicia o código se a altura inserida for inválida
        except(ValueError):
            print("Altura inválida. Tente novamente")
    executar = True # variável que irá definir se o próximo bloco irá rodar
    while executar:
            genero = input('\nInsira seu gênero, digite "m" para mulher e "h" para homem: ') #pede o genero do usuario
            # calculando o peso ideal de acordo com o genero escolhido utilizando if
            if genero == 'm':
                peso_idealM = (62.2 * altura) - 44.7
                print(f'\nSeu peso ideal é: {peso_idealM:.2f} kg.')
                executar = False # torna a condição de execução falsa
            elif genero == 'h':
                peso_idealH = (72.7 * altura) - 58
                print(f'\nSeu peso ideal é: {peso_idealH:.2f} kg.')
                executar = False
            # o bloco a seguir não tornará a condição falsa
            else:
                print("Gênero inválido. Tente novamente.")

# exercicio 14
def exercicio_4():
    while True:
        try:
            # coletando o peso de peixes
            peso = float(input("Este programa calculará o peso de peixes excedido e a multa que deverá ser paga. Insira o peso dos peixes (em quilos):\n"))
            # verificando se o peso está acima ou abaixo do regulamento
            if peso <= 50: 
                print("\nO peso não está acima do estabelecido pelo regulamento. Não há multa.")
            else: # irá calcular o excesso e a multa
                excesso = peso - 50
                multa = excesso * 4.00
                # mostrando os dados
                print(f"\nO valor de quilos excedido é: {excesso:.2f}\nO valor da multa a ser paga é: {multa:.2f}")
            break
        except(ValueError):
            print("Peso inválido. Tente novamente")
     
# menu para escolher o exercício desejado
def main(): #pagina principal do programa
    print("Escolha o programa que deseja rodar")
    print("1. Calcular Operações (ex. 11)\n2. Calcular peso ideal geral (ex.12)\n3. Calcular peso ideal baseado em seu gênero (ex. 13)\n4. Verficar resultados de pesca (ex.14)")
    
    opcao = int(input("Digite o número do programa que deseja utilizar: ")) # recolhe a opcao que usuario escolher

    if opcao == 1:
        exercicio_1()
    elif opcao == 2:
        exercicio_2()
    elif opcao == 3:
        exercicio_3()
    elif opcao == 4:
        exercicio_4()
    else:
        print("Opção inválida. Digite 1, 2 ou 3")

if __name__ == "__main__":
    main()
