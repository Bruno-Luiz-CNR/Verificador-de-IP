import re
import json
from urllib.request import urlopen

print("#" * 60)
print("#" * 60)
print("#" * 60)
while True:
    print("[1] - Verificar IP")
    print("[2] - sair do sistema")
    resp = int(input("Digite a opção: ")) # inserir opção de escolha
    if resp == 1: # caso seja a opção 1 seguira com o procedimento de visualização
        ipdigitado = input("Digite o IP a ser verificado: ")
        url = "https://ipinfo.io/"  # url a ser verificada
        resp = urlopen(url + ipdigitado)  # abrindo a url
        dados = json.load(resp)  # json ira abrir o scrip e colocara em dados
        ip = dados['ip']
        org = dados['org']
        cid = dados['city']
        pais = dados['country']
        regiao = dados['region']
        local = dados['loc']
        print('Segue detalhamento : \n')
        print('ip: {0}\nRegião: {1}\nPais: {2}\nOrg: {3}\nCidade: {4}\nLocal: {5}\n'.format(ip,regiao,pais,org,cid,local))
        print("-" * 60)
        print("\n")
    else:
        break


