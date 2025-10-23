import random

def anagramapalavra(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    return ''.join(letras)

entrada = input("Digite uma palavra: ")
print("Anagrama:", anagramapalavra(entrada))