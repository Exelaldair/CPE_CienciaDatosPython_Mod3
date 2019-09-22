import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

aref_nasdaq = html_soup.find('a', title="Nasdaq")
nasdaq = float(aref_nasdaq.find("span").contents[0].replace(',',''))
print(nasdaq)

aref_gold = html_soup.find('a', title="Gold")
gold = float(aref_gold.find("span").contents[0].replace(',',''))
print(gold)

aref_silver = html_soup.find('a', title="Silver")
silver = float(aref_silver.find("span").contents[0].replace(',',''))
print(silver)


#print(html_contents)

#arefs = html_soup.find_all('a', class_="C(black) Fw(500) Fz(m) Td(n) Pend(34px) Pstart(10px) D(b)"),  #,  class_='Carousel-Slider Pos(r) Whs(nw)')
'''
arefs = html_soup.find_all('a', title="Nasdaq")
print(arefs)
for aref in arefs:
    print(aref)
    span = aref.find("span")
    print(span.contents[0])
    print(aref)
'''
# Nasdaq
# <a aria-label="Nasdaq has decreased by -0.80% or -65.21 points to 8,117.67 points" href="/quote/^IXIC?p=^IXIC" title="Nasdaq" class="C(black) Fw(500) Fz(m) Td(n) Pend(34px) Pstart(10px) D(b)" data-reactid="15"><!-- react-text: 16 -->Nasdaq<!-- /react-text --><span class="Trsdu(0.3s) Fz(s) Mb(0px) D(b)" data-reactid="17">8,117.67</span><span class="Trsdu(0.3s) Fz(s) D(b) C($dataRed)" data-reactid="18">-0.80%</span></a>

#nasdaq_span = html_soup.find('span', class_="Trsdu(0.3s) Fz(s) Mb(0px) D(b)")
#print(nasdaq_span.contents[0])

#
#<a aria-label="Gold has increased by 1.21% or 18.20 points to 1,524.40 points" href="/quote/GC=F?p=GC=F" title="Gold" class="C(black) Fw(500) Fz(m) Td(n) Pend(34px) Pstart(10px) D(b)" data-reactid="30"><!-- react-text: 31 -->Gold<!-- /react-text --><span class="Trsdu(0.3s) Fz(s) Mb(0px) D(b)" data-reactid="32">1,524.40</span><span class="Trsdu(0.3s) Fz(s) D(b) C($dataGreen)" data-reactid="33">+1.21%</span></a>
#title="S&amp;P 500"
#gold_span = html_soup.find('span', class_="Trsdu(0.3s) Fz(s) Mb(0px) D(b)")
#print(gold_span.contents[0])
