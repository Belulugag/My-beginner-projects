import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.imdb.com/title/tt0367594/?ref_=nv_sr_srsg_0')
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1').getText()

desc = soup.find(name='span', class_='GenresAndPlot__TextContainerBreakpointL-sc-cum89p-1 eqlIrG').getText()

team = soup.find_all(name='a', class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
team = [i.getText() for i in team]
def opisanie():
    global team,title,desc
    print(f'Film name: {title}')
    print(f'Description: {desc}')
    print('Directed by:', team[0])
    print('Writers:', *team[1:3])
    print('Stars:', *team[3:6])
movies = soup.find_all(name='td', class_='titleColumn')
def TOP_250():
    global movies
    response = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    soup = BeautifulSoup(response.text, 'html.parser')
    with open("films1.txt", 'w', encoding='utf-8') as file:
        for i in range(len(movies)):
            print(f'{i + 1}. {movies[i].a.text}', file=file)
opisanie()
