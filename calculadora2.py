def opcao():
  valida = False
  while valida == False:
    try:
      operacao = int(input("\n1. Soma\n" + "2. Subtração\n" +"3. Multiplicação\n"
                  +"4. Divisão\n" +"0. Sair\n" +"Escolha a operação: "))
      if operacao >= 0 and operacao < 5:
        valida = True
        return operacao
      else:
        print("\033[31mFavor digitar umas das opções informadas.\033[m")
    except:
      print('\033[31mFavor digitar um dos números inteiros informados.\033[m')


def calculadora(operacao):
  if operacao == 0:
    print("\033[32mSaindo do programa. Até a próxima.\033[m")
    exit()
  while operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4:
    try:
      valor1 = int(input("Digite o primeiro valor: "))
      valor2 = int(input("Digite o segundo valor: "))
      #print(valor1,valor2)

      if operacao == 1:
        print(valor1 + valor2)
        break
      elif operacao == 2:
        print(valor1 - valor2)
        break
      elif operacao == 3:
        print(valor1 * valor2)
        break
      else:
        if valor2 <= 0:
          print("\033[33mUm valor não pode ser dividido por '0'\033[m")
        else:
          print(valor1 / valor2)
      break
    except:
      print("\033[31mVocê precisa digitar valores inteiros, vamos começar novamente.\033[m\n")
      calculadora(operacao)


print("\nCalculadora")

operacao =opcao()
calculadora(operacao)