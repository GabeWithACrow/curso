import random

def exibir_numeros(qtde_jogos):
    for j in range(qtde_jogos):
        print("jogo:",j+1)
        x = 1
        numeros = ""
        for x in range(6):
            numeros = numeros + " " + str(random.randrange(1, 60, 1))
        print(numeros)

if __name__ == "__main__":
    q=int(input("quantos jogos ?"))
    exibir_numeros(q)