palavra = input("Digite sua palavra para verificação de palíndromo: ")


palindromo_array = []
palindromo_str = ''

# Vamos definir uma função para inverter a palavra:

def inverte():
    for i in range(1, len(palavra) + 1):
         palindromo_array.append(palavra[-i])

# Agora definimos uma função para verificar a nossa premissa do palíndromo;

def verifica(palindromo_str):
    for i in range(0, len(palindromo_array)):
        palindromo_str += palindromo_array[i]

    if (palindromo_str == palavra):
        print("Sim! É um palíndromo!")
    else:
        print("Não, esta palavra não é um palíndromo.")

inverte()

verifica(palindromo_str)
