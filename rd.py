import requests
from bs4 import BeautifulSoup

def ruler_dev():
    url = 'http://haryanarural.gov.in/en/schemes'
    
    r = requests.get(url)
    html_content = r.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    links = []
    schemes = []
    
    for ul in soup.find_all('ul'):
        for li in ul.find_all('li'):
            a = li.find('a')
            links.append(a['href'])
            schemes.append(a.get_text())
            
    string = 'http://haryanarural.gov.in'
    string += '{0}'
    links = [string.format(i) for i in links] 
    links = links[21:29]
    schemes = schemes[21:29]
    return zip(schemes, links)


r = ruler_dev()
for i,j in r:
    print(f"Scheme Name :-{i}, Scheme Link:-{j}")