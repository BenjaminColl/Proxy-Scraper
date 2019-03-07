import requests, os, random, traceback, json
from itertools import cycle
from fake_useragent import UserAgent as UA
from bs4 import BeautifulSoup

class PS(object):
    def __init__(self):
        self.UA = UA()
        self.s = requests.session()
        self.s.headers.update(({'User-Agent':self.UA.random}))
        self.base = 'https://www.sslproxies.org/'

    def proxies(self):
        self.pproxies = []
        url = self.base
        r = self.s.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        proxies_table = soup.find(id='proxylisttable')
        for row in proxies_table.tbody.find_all('tr'):
            self.pproxies.append({'ip': row.find_all('td')[0].string,'port': row.find_all('td')[1].string})
        for i in range(100):
            getprox = self.prox()
            makeprox = self.pproxies[getprox]
            f = open(os.path.join('Proxies.txt'),'a')
            f.write(makeprox['ip'] +':'+ makeprox['port'] + '\n')
            f.close()
        print('x100 Proxies have been saved to: Proxies.txt')

    def prox(self):
        return random.randint(0, len(self.pproxies) - 1)

if __name__ == '__main__':
    a = PS()
    a.proxies()
