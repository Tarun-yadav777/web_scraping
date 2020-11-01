import requests
from bs4 import BeautifulSoup


def sports():
    url = 'https://yas.nic.in/sports/schemes'
    
    r = requests.get(url)
    html_content = r.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    links = []
    schemes = []
   
    
    for i in soup.find_all('h2'):
        link = i.find('a',href=True)
        if link is None:
            continue
        links.append(link['href'])
    
    string = 'https://yas.nic.in'
    string += '{0}'
    links = [string.format(i) for i in links] 
    
            
    for i in soup.find_all('h2'):
        link = i.find('a')
        if link is None:
            continue
        schemes.append(link.get_text())
    return zip(schemes, links)
    
r = sports()
for i,j in r:
    print(f"Scheme Name :-{i}, Scheme Link:-{j}")
    

        