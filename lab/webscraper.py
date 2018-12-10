import bs4, requests
#coreyjones


#----------------------------------------------------------------------
def getAmazonPrice(productUrl):
    """"""
    res = requests.get(productUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('some code to select') #css selecter
    return elems[0].text.strip()
    

price = getAmazonPrice('some url')
print('The price is ' + price)



    
    