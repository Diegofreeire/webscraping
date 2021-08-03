from scraping import webscraping

if __name__ == "__main__":
    web_scraping = webscraping()
    web_scraping.getPrecificacao()
    web_scraping.parseToHtml()
    web_scraping.createDataFrame()
    web_scraping.convertToDict()
    web_scraping.writeJsonFile()
    web_scraping.writeCsvFile()