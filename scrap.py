from bs4 import BeautifulSoup as bs
import requests

r = requests.get('https://pueblosoriginarios.com/lenguas/tzotzil.php')

soup = bs(r.text, 'html.parser')



table = soup.find("table", id="tzotzil")
tr_store = [x for x in table.children if x.name == 'tr']

words = []
for tr in tr_store:
    words.append(tr.text)


print(words)