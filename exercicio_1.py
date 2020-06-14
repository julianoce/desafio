centena = {0: "", 1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seissentos",
           7: "setessentos", 8: "oitocentos", 9: "novecentos"}

dezena = {2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta", 8: "oitenta",
          9: "noventa"}

unidade = {0: "", 1: "um", 2: "dois", 3: "tres", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito",
           9: "nove"}

dezena_diff = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
               17: "dezessete", 18: "dezoito", 19: "dezenove"}

milhares_diff = {0: "mil", 1: "milhao", 2: "milhoes", 3: "bilhao", 4: "bilhoes"}


def parser_centena(num):
    string = []
    if num == 100:
        string.append("cem")
    else:
        num_div = num / 100
        num_mod = num % 100
        if num_div > 0:
            string.append(centena[num_div])
            if num_mod > 0:
                string.append("e")
        string = parser_dezena_unidade(num_mod, string)

    return string


def parser_dezena_unidade(num, string):
    if num in dezena_diff:
        string.append(dezena_diff[num])
    else:
        num_d = num / 10
        num_m = num % 10
        if num_d > 0:
            string.append(dezena[num_d])
            if num_m > 0:
                string.extend("e")
        if num_m > 0:
            string.append(unidade[num_m])
    return string


def parser_mil(num):
    string = []
    if num == 1000:
        string.append(milhares_diff[0])
        return string, 0
    else:
        num_div = num / 1000
        num_mod = num % 1000

        if num_div > 0:
            string.extend(parser_centena(num_div))
            string.append(milhares_diff[0])
        return string, num_mod


def parser_milhao(num):
    string = []

    num_div = num / 1000000
    num_mod = num % 1000000

    if num_div > 0:
        string.extend(parser_centena(num_div))
        if num_div == 1:
            string.append(milhares_diff[1])
        else:
            string.append(milhares_diff[2])
    return string, num_mod


def parser_reais(valor):
    string = []
    string_list = []
    palavra_final = ""
    string_1, resto = parser_milhao(valor)
    string_2, resto = parser_mil(resto)
    string_3 = parser_centena(resto)
    string.extend((string_1, string_2, string_3))
    for x in string:
        for y in x:
            string_list.append(y)
    for i in range(len(string_list)):
        palavra_final += string_list[i] + " "

    if valor == 1:
        return palavra_final + "real "
    elif valor == 0:
        return ""
    else:
        return palavra_final + "reais "


def parser_centavos(valor):
    string = parser_centena(valor)
    palavra_final = ""
    for i in range(len(string)):
        palavra_final += string[i] + " "
    if valor == 0:
        return ""
    elif valor == 1:
        return palavra_final + "centavo"
    else:
        return palavra_final + "centavos"


entrada = input("Digite um numero em que deseja converter ou '1' para sair: ")
while entrada != "1":
    try:
        real, centavo = entrada.split(",")
        if len(real) > 9 or len(real) < 1 or len(centavo) != 2:
            print("Numero invalido, tente novamente outro numero")
        else:
            real = parser_reais(int(real))
            palavra_centavo = parser_centavos(int(centavo))
            if centavo == "00":
                print(real)
            else:
                if centavo and real:
                    print(real + "e " + palavra_centavo)
                else:
                    print(palavra_centavo)
    except:
        print("Numero invalido, tente novamente outro numero")
    entrada = input("Digite um numero em que deseja converter ou '1' para sair: ")
