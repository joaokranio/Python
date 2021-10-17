#  Criar um programa para receber e armazenar itens e valores, somá-los em uma
#  possível compra e dividir o valor total em determinada quantidade de pessoas

# quantidade de produtos comprados
pr = int(input("Quantos produtos foram comprados: \n"))
i = 0
tun = 0  # Total UNIDADE
t1 = 0  # Total parcial unidade
t2 = 0  # total parcial peso
tp = 0  # total por peso

while i < pr:
    tipo = int(input("Produto vendido por: Unidade - 1  , Peso - 2\n"))
    if tipo == 1:  # tipo 1, unidade selecionado

        qt = float(input("Quantidade do produto: \n"))  # quantidade
        vq = float(input("Valor por unidade: \n"))  # valor por unidade
        t1 = qt * vq  # total parcial unidade
        print("Valor R$: ", "%.2f" % t1, "\n")
        tun = t1 + tun  # total unidade
        # print("Valor R$: ", "%.2f" % tun, "\n")

        i = i + 1  # acrescimo de contador
    elif tipo == 2:  # tipo dois Peso
        pe = float(input("Peso comprado(KG):  \n"))  # peso que foi comprado
        vp = float(input("Valor por KG: \n"))  # valor por peso
        t2 = pe * vp  # total parcial peso
        print("Valor R$: ", "%.2f" % t2, "\n")
        tp = t2 + tp  # total peso
        # print("Valor R$: ", "%.2f" % tp, "\n")
        i = i + 1  # acrescimo de contador

    else:
        print("Formato incorreto")
tg = tun+tp  # total geral
print("Valor TOTAL R$: ", "%.2f" % tg, "\n")

p = int(input("Quantas pessoas dividiram a compra: \n"))
conta = tg / p

print("Valor Individual R$: ", "%.2f" % conta, "\n")


# Exercício 3 da lista - Resposta R$ 51.73
