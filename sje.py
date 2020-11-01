import requests
from bs4 import BeautifulSoup


def social_justice():
    url = 'http://socialjustice.nic.in/SchemeList/index?mid=24541'
    
    r = requests.get(url)
    html_content = r.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    links = []
    schemes = []
    
    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):
            a = td.find('a')
            links.append(a['href'])
            schemes.append(a['title'])
            
    string = 'http://socialjustice.nic.in'
    string += '{0}'
    links = [string.format(i) for i in links] 
    return zip(schemes, links)


r = social_justice()
for i,j in r:
    print(f"Scheme Name :-{i}, Scheme Link:-{j}")