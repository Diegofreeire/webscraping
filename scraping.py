import json
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime, date

class webscraping:
    #-------
    #| Construtor para inicializar o selenium e suas configurações
    #-------  
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.options = Options()
        self.options.headless = True

    #-------
    #| Função p/ abrir o site requerido e buscar o bloco html
    #------- 
    def getPrecificacao(self):
        try:
            url = "https://br.advfn.com/bolsa-de-valores/bovespa/enjoei-on-ENJU3/cotacao"
            self.browser.get(url)
            self.res = self.browser.find_element_by_xpath("//*[@id='quote_top']")
            self.html_content = self.res.get_attribute("outerHTML")
            self.browser.quit()
        except:
            print("An exception occurred") 
            self.browser.quit()
    
    #-------
    #| Função responsável por parsear o html e filtrar os elementos
    #------- 
    def parseToHtml(self):
        try:
            self.tds = []
            self.soup = BeautifulSoup(self.html_content, 'html.parser')
            for td in self.soup.select(".TableElement td span"):
                if td.text != "":
                    self.tds.append(td.text)
        
            self.browser.quit()
        except:
            print("An exception occurred") 
            self.browser.quit()

    #-------
    #| Criação dos headers e DataFrame
    #------- 
    def createDataFrame(self):
        self.headers = [
                "tipo_ativo",
                "variacao_dia_p",
                "variacao_do_dia_avg",
                "ultimo_preco",
                "hora",
                "preco_de_abertura",
                "preco_min",
                "preco_max",
                "fech_hoje",
                "fech_anterior",
                "melhor_preco_compra",
                "melhor_preco_venda",
                "spread_de_preco",
                "num_de_negocios",
                "vol_acoes_negociadas",
                "preco_med",
                "vol_financeiro",
                "ultimo_negocio",
                "qtd_acoes_negociadas",
                "preco_negociado",
                "moeda"
            ]
        self.df_full = [self.headers, self.tds]
        column_name = self.df_full.pop(0)
        self.df = pd.DataFrame(self.df_full, columns=column_name)
        self.df.insert(0, "data", datetime.today().isoformat(), True)

    #-------
    #| Transformação do DataFram en Dicionário
    #------- 
    def convertToDict(self):
        self.dictionary = self.df.to_dict('records')
        print(self.dictionary)

    #-------
    #| Criação arquivo JSON
    #------- 
    def writeJsonFile(self):
        js = json.dumps(self.dictionary)
        fp = open('./json/priceTracking.json', 'w')
        fp.write(js)
        fp.close()
    
    #-------
    #| Criação arquivo CSV
    #------- 
    def writeCsvFile(self):
        df = pd.read_json('./json/priceTracking.json')
        df.to_csv('./csv/priceTracking.csv', index=None)
