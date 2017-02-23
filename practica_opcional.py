#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Client web per https://www.packtpub.com/packt/offers/free-learning/
@autor: Sergio
'''
import urllib2
from bs4 import BeautifulSoup

class Client(object):
    def get_web(self,page):
        """ Baixar-se la web """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    # TODO: Buscar el text
    def search_text(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div", "dotd-title") # Buscar un div que tingui aquesta clase
        #title = elements.get_text("h2") # Per agafar el contingut del HTML
        resultats = []
        for element in elements:
            data = element.find("h2")
            title = data.text
            title = title.strip() # Quitar espacios en blanco de los lados
        return title

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        resultat = self.search_text(web)
        # FIXME: Imprimir resultats
        print resultat

if __name__ == "__main__":
    client = Client()
    client.main()
