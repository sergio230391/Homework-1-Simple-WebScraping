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
        
        return elements

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        resultat = self.search_text(web)
        # FIXME: Imprimir resultats
        print len(resultat)

if __name__ == "__main__":
    client = Client()
    client.main()
