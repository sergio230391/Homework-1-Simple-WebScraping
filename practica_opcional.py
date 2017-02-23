#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Client web per https://www.packtpub.com/packt/offers/free-learning/
@autor: Sergio
'''
import urllib2
from bs4 import BeautifulSoup

import subprocess

class Client(object):
    def get_web(self,page):
        """ Baixar-se la web """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self,html):
        """ Buscar el text """
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", "dotd-title") # Buscar un div que tingui aquesta clase
        title = elements.text
        title = title.strip() # Quitar espacios en blanco de los lados
        return title

    def notification(self,title):
        """ Notificació del nou llibre """
        subprocess.Popen(['notify-send', "Nuevo libro gratuito: " + title])

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning/')
        resultat = self.search_text(web)
        # FIXME: Imprimir resultats
        self.notification(resultat)
        print resultat

if __name__ == "__main__":
    client = Client()
    client.main()
