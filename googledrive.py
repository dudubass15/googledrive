#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os

#Pega a entrada do usuário (site) e coloca em uma variável
website = raw_input('Digite o endereco: ')

if website == 'www.google.com.br':
    c = requests.get('http://' + website)

    #Verifica se conseguiu acessar o site
    if c.status_code == 200:
        nome_search = 'google+drive'
        idgoogle_search = '009546483759896444502'
        url_search = '/search?start=0&num=10&q='+nome_search+'&cx='+idgoogle_search
        result_search = website + url_search
        print(result_search)
    else:
        print "Error !"
        #print c.status_code
elif website == 'www.google.com':
    c = requests.get('http://' + website)

    #Verifica se conseguiu acessar o site
    if c.status_code == 200:
        nome_search = 'google+drive'
        idgoogle_search = '009546483759896444502'
        url_search = '/search?start=0&num=10&q='+nome_search+'&cx='+idgoogle_search
        result_search = website + url_search
        print(result_search)
    else:
        print "Error !"
    #print c.status_code
else:
    print "Endereco invalido!"

os.system("pause");