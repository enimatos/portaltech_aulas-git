valido = False
nome = input("Digite seu nome completo: ")
while (valido == False):
    try:
        ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
        if ano >= 1922 and ano <= 2021:
            idade = 2022 - ano
            print(f'\n\033[32mOlá {nome}, em 2022 você completa {idade} anos.\033[m')
            valida = True
            break
        else:
            valida = False
    except:
        print("\033[31mTipo de dado inválido, favor digitar dígitos numéricos.\033[m")