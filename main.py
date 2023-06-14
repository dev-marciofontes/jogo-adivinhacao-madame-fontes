import random
import time


print("\n#### Bem-Vindo(a) ao jogo de adivinhação da Madame Fontes ####")
print(" ")
print("Defina os intervalos para que os espíritos escolham um número!!")

numero_minimo = int(input("Qual o número mínimo?\n"))
numero_maximo = int(input("Qual o número máximo?\n"))

print(
    "\nÓtimo! Os espíritos estão escolhendo a sua quantidade de tentativas "
    "para que seja justa, baseada nos seus intervalos..."
)

time.sleep(2)

diferenca = numero_maximo - numero_minimo
tentativas = 0

if diferenca <= 5:
    tentativas = 1
    print("\nHum, quer pagar de pessoa espertinha né? Você só tem uma tentativa!")
elif numero_maximo < 10:
    tentativas = random.randint(1, 3)
elif 10 < numero_maximo < 25:
    tentativas = random.randint(2, 5)
elif 25 < numero_maximo < 50:
    tentativas = random.randint(4, 8)
else:
    tentativas = random.randint(7, 10)

print(f"\nEles escolheram... Sua quantidade de tentativas é {tentativas}")

numero_sorteado = random.randint(numero_minimo, numero_maximo)

print("Os espiritos estão escolhendo um número...")
time.sleep(2)

print("\nOs espíritos já escolheram um número! Agora você deve tentar acertar:")

while True:
    tentativa = int(
        input(f"Digite um número entre {numero_minimo} e {numero_maximo}.\n")
    )

    if tentativa == numero_sorteado:
        print(
            "Uauuu, você venceu a Madame Fontes! Parabéns, "
            "este era exatamente o número que os espíritos me passaram...\n"
        )
        break
    else:
        tentativas -= 1
        if tentativas == 0:
            print(
                "\nVocê não acertou o número e os espíritos não irão mais "
                + "permitir novas tentativas! HAHAHAH."
            )
            print(f"O número sorteado era: {numero_sorteado}\n")
            print(
                "Tente novamente outro dia. A Madame Fontes agradece "
                + "a sua participação!"
            )
            break
        else:
            if numero_maximo > 12:
                if tentativa > numero_sorteado:
                    print(
                        "Huuum... Este não é o número... tente de novo! "
                        "Tente um menor do que esse... "
                        f"Você ainda tem {tentativas} tentativas!"
                    )
                elif tentativa < numero_sorteado:
                    print(
                        "Huuum... Este não é o número... tente de novo! "
                        "Tente um número maior do que esse... "
                        f"Você ainda tem {tentativas} tentativas!"
                    )
            else:
                print(
                    "Huuum... Este não é o número... tente de novo! Você ainda"
                    f" tem {tentativas} tentativas!"
                )
