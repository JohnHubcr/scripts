import os
import requests
from bs4 import BeautifulSoup

os.system('clear')
print ('='*31)
print ('| Offical Kali Linux RepoList |')
print ('='*31 + '\n')
url = 'https://http.kali.org/README.mirrorlist'
page = requests.get(url)
page = page.content
list = []
soup = BeautifulSoup(page, 'html.parser')
for link in soup.find_all('a'):
    list.append(link.get('href'))

for item in list:
    if 'meta' in item:
        pass
    elif 'README' in item:
        repo = item.strip('README')
        print ('deb ' + repo + ' kali-rolling main contrib non-free')
