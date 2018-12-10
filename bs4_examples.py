import os, selenium, bs4, requests, pprint, re
from fake_useragent import UserAgent


url = 'https://www.amazon.com/gp/product/B00WJ049VU/ref=s9_acsd_simh_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=XPW90D7Y5J2A4PGTZ61V&pf_rd_r=XPW90D7Y5J2A4PGTZ61V&pf_rd_t=101&pf_rd_p=77a4a915-4522-4f1b-a04f-1d71908c15fa&pf_rd_p=77a4a915-4522-4f1b-a04f-1d71908c15fa&pf_rd_i=156116011'
headerss = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
headersss ={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'}
ua = UserAgent()


uniua = ua.random

headers = "{'User-Agent': '%s'}" % (uniua)
print(headers)
print(headerss)
s = requests.Session()
res = s.get(url, headers=headersss)

res.raise_for_status()

os.chdir('c:\\delicious')

#playFile = open('webpage.txt', mode='wb', buffering=2)
#for chunk in res.iter_content(100000):
    #playFile.write(chunk)
#playFile.close()



pprint.pprint(res.headers)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

#pprint.pprint(soup)


#csoup = soup.select("[class~=a-size-medium a-color-price header-price]")

#for div in soup.select('class.a-size-medium.a-color-price.header-price'):
    #print(div.text)
    
css_path = '#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price'    
css_2path = '#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price'
css3_path = '#mediaNoAccordion .header-price'    



newcss = css_path.replace(' ', ' > ') 
print(css3_path)

csoup = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

#csoup = soup.select('div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
pprint.pprint(csoup)


#for node in soup.find_all('price'):
    ##(attrs={'class': re.compile(r"^a-size-medium a-color-price header-price\b.*")})
    #print(node)
    
    
#pprint.pprint(csoup)
#pprint.pprint(soup.title)
#pprint.pprint(soup.head)

#esoup = soup.findParents("p")


#pprint.pprint(esoup)





