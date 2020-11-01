import requests
from bs4 import BeautifulSoup


def child():
    url = 'https://wcd.nic.in/schemes-listing/2419'
    
    r = requests.get(url)
    html_content = r.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    links = []
    schemes = []
    
    for ol in soup.find_all('ol'):
        for li in ol.find_all('li'):
            a = li.find('a')
            links.append(a['href'])
            schemes.append(a.get_text())
            
    string = 'https://wcd.nic.in'
    string += '{0}'
    links = [string.format(i) for i in links] 
    
    return zip(schemes, links)


r = child()
for i,j in r:
    print(f"Scheme Name :-{i}, Scheme Link:-{j}")