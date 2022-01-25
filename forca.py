def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


palavra_secreta = "maça".upper()
letras_acertadas = ["_" for letra in palavra_secreta]

enforcou = False
acertou = False
erros = 0

print (letras_acertadas)

while (not acertou and not enforcou):


    chute = input("Digita a letra ")
    chute = chute.strip().upper() #strip retira espaços na palavra

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index +=1 #rotina para verificar posição das letras

    else:
        erros += 1
    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

    if(acertou):
        print("Você acertou!")
    else:
        print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
