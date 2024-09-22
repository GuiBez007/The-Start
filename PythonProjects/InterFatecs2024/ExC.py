# Password

def Verification(password):
    # se maior que 20 ou menor que 1 finaliza
    if len(password) < 1 or len(password) > 20:
        return

    # lista de caracteres inválidos e inicialização de booleanos em False
    not_permited = '.,!?;: áéíóúâêôãõàçÁÉÍÓÚÂÊÔÃÕÀÇ'
    upper_check = lower_check = number_check = False

    if len(password) < 6 or len(password) > 15:
        return False
    else:
        # pega o valor numérico do caracter na tabela ASCII
        previous_char = ord(password[0])

        for char in password:

            # verifica se valor numérico do atual é o sucessor do anterior
            if ord(char) == previous_char + 1:
                return False
            previous_char = ord(char)

            # checa se não está na lista de caracteres não permitidos
            if char in not_permited:
                return False

            # verifica se as condições foram atendidas e muda seus valores para True
            if char.isupper() and upper_check == False:
                upper_check = True
            if char.islower() and lower_check == False:
                lower_check = True
            if char.isnumeric() and number_check == False:
                number_check = True

            # VERIFICAÇÃO GERAL
            if upper_check == True and lower_check == True and number_check == True:
                return True
        return False

# chama a função e pega o parâmetro (senha) com o usuário
print("{}.".format(Verification(input())))
