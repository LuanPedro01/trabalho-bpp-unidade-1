data = []

# função que faz tudo
def f(a, b=None):
    # essa função adiciona uma coisa
    if a != "":
        d = {}
        d["t"] = a
        if b == None:
            d["c"] = "duvidosa"
        else:
            d["c"] = b
        data.append(d)
    else:
        print("erro")


def func2():
    # lista tudo
    for i in range(0, len(data)):
        print("Texto:", data[i]["t"])
        print("Classificacao:", data[i]["c"])
        print("-------------------")


def analisar(txt):
    # analisa o texto
    score = 0

    if "FONTE" not in txt:
        score = score + 1
    if "!!!" in txt:
        score = score + 1
    if "URGENTE" in txt:
        score = score + 1
    if len(txt) < 10:
        score = score + 1

    if score == 0:
        return "confiavel"
    elif score == 1:
        return "duvidosa"
    else:
        return "falsa"


def add_manual():
    t = input("Digite o texto: ")
    c = input("Digite classificacao: ")

    if c == "":
        f(t)
    else:
        f(t, c)


def add_auto():
    t = input("Digite o texto: ")
    c = analisar(t)
    f(t, c)


def menu():
    while True:
        print("1 - adicionar manual")
        print("2 - adicionar automatico")
        print("3 - listar")
        print("4 - sair")

        op = input("opcao: ")

        if op == "1":
            add_manual()
        elif op == "2":
            add_auto()
        elif op == "3":
            func2()
        elif op == "4":
            break
        else:
            print("errado")


menu()
