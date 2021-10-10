import requests
from bs4 import BeautifulSoup

class Scrap:

    def __init__(self):
        print('Loading...')

    def pars(self,crypto):
        r = requests.get('https://coinmarketcap.com/currencies/'+crypto)

        with open("index.txt", "w", encoding='utf-8') as f:
            f.write(r.text)

        with open("index.txt", encoding='utf-8') as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        paragraphs = soup.find_all("p")

        return paragraphs

    def paragraphs_file(self,sitepars):
        with open("p.txt", "w", encoding='utf-8') as file:
            for p in sitepars:
                print(p.text+'\n')
                file.write('\n')
                file.write(p.text)
                file.write('\n')








print("1)bitcoin\n2)ethereum\n3)cardano\nChoose your crypto: ")

crypto = input()

scrapper = Scrap()
sitepars = scrapper.pars(crypto)
parag = scrapper.paragraphs_file(sitepars)


