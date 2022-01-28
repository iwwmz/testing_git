from bs4 import BeautifulSoup
import requests
import lxml
import re

#url = 'https://www.soe.com.ua/includes/disconnection_accidentpg.php?x=1&y=2022&typetermin=for_month&typeshut=2&rayons=11&dateshut=%20Request%20Method:%20POST%20Status%20Code:%20200%20OK%20Remote%20Address:%20193.110.17.157:443'


with open("D:/test_git/data.html", 'rb') as html:
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all('thead')[1]
    info = []
    for i in data:
        info.append(i.getText())
    date = re.search(r"[0-3][0-9]\.[0-1][0-9]\.[2][2]",str(info[0]))
    time = re.search(r"[0-2][0-9][:][0-5][0-9]", str(info[0]))
    print(date)
    print(time)
    print(info[0])





