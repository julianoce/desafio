from bs4 import BeautifulSoup
import requests

entrada = input("Digite o codigo do aeodromo que deseja analisar ou '1' para sair: ")

while entrada != "1":
    try:
        print("Fazendo requisicao para a pagina...")

        url = "https://www.aisweb.aer.mil.br/?i=aerodromos&codigo=" + entrada
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        metar_content = soup.find_all('h5', {'class': 'mb-0 heading-primary'})[0].find_next_sibling("p").get_text()
        taf_content = soup.find_all('h5', {'class': 'mb-0 heading-primary'})[1].find_next_sibling("p").get_text()

        nascer_sol = soup.find('sunrise').contents[0]
        por_do_sol = soup.find('sunset').contents[0]

        carta = soup.find_all('h4', {'class': 'heading-primary'})[3]
        rotas = soup.find_all('h4', {'class': 'heading-primary'})[4]

        cartas_arr = []

        while carta.find_next_sibling("h4") != rotas:
            cartas_arr.append(carta.find_next_sibling("h4").get_text())
            carta = carta.find_next_sibling("h4")

        print("----------")
        print("Cartas:")
        for c in cartas_arr:
            print(c + " ")
        print("\nHorarios do Sol")
        print("Nascer do Sol: {}".format(nascer_sol) + " " + "Por do Sol: {}".format(por_do_sol) + "\n")
        print("TAF:\n {}".format(taf_content))
        print("\nMETAR:\n {}\n".format(metar_content))
        print("----------")
    except:
        print("Codigo invalido, tente novamente outro codigo")

    entrada = input("Digite o codigo do aeodromo que deseja analisar ou '1' para sair: ")
