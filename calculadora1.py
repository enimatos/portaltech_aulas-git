
def calculadora(operacao):
  if operacao == 0:
    exit()
    return 0
  valor1 = int(input("Digite o primeiro valor: "))
  valor2 = int(input("Digite o segundo valor: "))
  if operacao == 1:
    return valor1 + valor2
  elif operacao == 2:
    return valor1 - valor2
  elif operacao == 3:
    return valor1 * valor2
  elif operacao == 4:
    if valor2 <= 0:
      return "Um valor não pode ser dividido por '0'"
    else:
      return valor1 / valor2
  else:
    return "Valor de operação inválido."


print("Calculadora")
oper=(int(input("1. Soma\n" +
      "2. Subtração\n" +
      "3. Multiplicação\n" +
      "4. Divisão\n" +
      "Escolha a operação: ")))



resultado = (calculadora(oper))
print("O resultado da operação é: ",resultado)