import requests
from bs4 import BeautifulSoup

def get_netflix_movie_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('h1', {'data-uia': 'title'})
        title = title_tag.text.strip() if title_tag else "Название не найдено"

        description_tag = soup.find('span', {'dir': 'ltr'})
        description = description_tag.text.strip() if description_tag else "Описание не найдено"
        actors = []
        info_block = soup.find('div', class_=lambda x: x and 'detail-list-wrapper' in x)
        if info_block:
            for element in info_block.find_all('span'):
                text = element.text.strip()
                if "В главных ролях" in text:
                    actor_names_str = text.split("В главных ролях")[-1].strip()
                    actors = [name.strip() for name in actor_names_str.split(',') if name.strip()]
                    break
        if not actors:
            actors = ["Актеры не найдены"]
        print(f"Название: {title}")
        print(f"Описание: {description}")
        print(f"Актеры: {', '.join(actors)}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    except Exception as e:
        print(f"Произошла ошибка при обработке страницы: {e}")

movie_url = input("Введите ссылку на фильм Netflix: ")
get_netflix_movie_info(movie_url)
