import random
import string
from time import sleep

def boas_vindas():
    print("=" * 30)
    print("\tBEM-VINDO AO GERADOR DE SENHAS!")
    print("=" * 30)

def random_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    boas_vindas()
    while True:
        try:
            tamanho_senha = int(input("Tamanho da senha: "))
            quantidade = int(input("Quantidade de senhas: "))
            
            print("=" * 30)
            print("\tGERANDO SENHAS...")
            print("=" * 30)
            
            sleep(0.5)
            
            for i in range(quantidade):
                senha = random_senha(tamanho_senha)
                print(f"\tSenha {i+1}: {senha}")
            
            print("=" * 30)
            break
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")

            
if __name__ == '__main__':
    main()