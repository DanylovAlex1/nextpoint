from bs4 import BeautifulSoup
import requests
import datetime

from .models import Usd



def get_html(url, header):
    html = requests.get(url=url, headers=header)
    return html


def get_content(html):
    currency = []
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='mb-valcli--archive--table')
    rows = table.find_all('tr')
    for row in rows:
        dat = row.find_next('td')
        date = dat.get_text()
        adat = dat.find_next_sibling('td')
        a = adat.get_text()
        b = adat.find_next_sibling('td').get_text()
        currency.append({'date': date,
                         'A': a, 'B': b})
    return currency

def getDateFormatted(dt):
    dtt = datetime.datetime.strptime(dt, '%d.%m.%Y')
    date = dtt.strftime("%Y-%m-%d")
    return date



def saveToDB(obj=None):
    if obj:
        cnt=0
        for row in obj:
            cnt+=1
            dt = row['date']
            a = row['A']
            b = row['B']
            date= getDateFormatted(dt)
            p=Usd(date=date, buy=a, sale=b)
            p.save()

    else:
        print('Values are not present')

    return cnt

