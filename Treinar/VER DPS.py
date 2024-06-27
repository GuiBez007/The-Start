print("Olá")
import os
nome = input('Qual seu nome? ')
os.system('cls')
print('Blz então {}'.format(nome))


import pyautogui
import time

def limpar_console():
    # Ajuste os valores de acordo com a sua necessidade
    pyautogui.hotkey('ctrl', 'l')  # Pressiona Ctrl + L para limpar o console
    time.sleep(0.5)  # Aguarda um curto período para garantir que o comando seja executado

# Exemplo de uso
limpar_console()

