import requests
from bs4 import BeautifulSoup as bs
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def download(url):
    response = requests.get(url, stream=True)
    r = open('C:\\Users\\user\\Desktop\\images\\' + url.split("/")[-1], 'wb', )
    for value in response.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers=headers)
        soup = bs(response.text, 'lxml')
        # print(soup)
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for item_data in data:
            # name = item_data.find('h4', class_='card-title').text.replace('\n', '')
            # price = item_data.find('h5').text
            # url_img = f'{"https://scrapingclub.com"}' + item_data.find('img', 'card-img-top img-fluid').get('src')
            # print(f'{name} ===  \n{price}  ===  \n{url_img}\n')
            card_link = f'{"https://scrapingclub.com"}' + item_data.find('a').get('href')
            # print(card_link)
            yield card_link


def get_arr():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = bs(response.text, 'lxml')
        data = soup.find('div', class_='card mt-4 my-4')
        name = data.find('h3', 'card-title').text
        price = data.find('h4').text
        text_p = data.find('p', 'card-text').text
        url_img = f'{"https://scrapingclub.com"}' + data.find('img', 'card-img-top img-fluid').get('src')
        download(url_img)
        yield name, price, text_p, url_img
