# exercicios para a materia de linguagens e programacao

# exercicio 11
def exercicio_1():
    while True: # utilizei while para que, caso seja inserido um valor invalido, o codigo reincie
        try:
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
        except ValueError:
            print("Valor Inválido. Tente Novamente")

# exercicio 12
def exercicio_2():
    try:
        altura = float(input("Descubra seu peso ideal! Insira sua altura (em metros): \n")) #pede a altura do usuario
        peso_ideal = (72.7 * altura) - 58
        print(f'O seu peso ideal é: {peso_ideal:.3f}')
    except ValueError:
        print("Altura inválida. Tente novamente")

# exercicio 13
def exercicio_3():
    while True: # loop para garantir que a altura inserida será valida
        try:
            altura = float(input("\nDescubra seu peso ideal!\nInsira sua altura (em metros): ")) # pede a altura do usuario
            break # reinicia o código se a altura inserida for inválida
        except ValueError:
            print("Altura inválida. Tente novamente")

    genero = str(input('\nInsira seu gênero, digite "m" para mulher e "h" para homem: ')) #pede o genero do usuario
    # calculando o peso ideal de acordo com o genero escolhido utilizando if
    if genero == 'm':
        peso_idealM = (62.2 * altura) - 44.7
        print(f'\nSeu peso ideal é: {peso_idealM:.2f} kg.')
    elif genero == 'h':
        peso_idealH = (72.7 * altura) - 58
        print(f'\nSeu peso ideal é: {peso_idealH:.2f} kg.')
    else:
        print("Gênero inválido. Tente novamente.")

# menu para escolher o exercício desejado
def main():
    print("Escolha o programa que deseja rodar")
    print("1. Calcular Operações (ex. 11)\n2. Calcular peso ideal geral (ex.12)\n3. Calcular peso ideal baseado em seu gênero (ex. 13)")
    
    opcao = int(input("Digite o número do programa que deseja utilizar: "))

    if opcao == 1:
        exercicio_1()
    elif opcao == 2:
        exercicio_2()
    elif opcao == 3:
        exercicio_3()
    else:
        print("Opção inválida. Digite 1, 2 ou 3")

if __name__ == "__main__":
    main()
    