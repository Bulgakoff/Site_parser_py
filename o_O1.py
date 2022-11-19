from requests import Session
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
work = Session()
work.get('https://quotes.toscrape.com/', headers=headers)
response = work.get('https://quotes.toscrape.com/login', headers=headers)
soup = bs(response.text, 'lxml')
token = soup.find('form').find('input').get('value')
data = {'csrf_token': token, 'username': 'noname', 'password': 'password'}
result = work.post('https://quotes.toscrape.com/login',
                   headers=headers,
                   data=data,
                   allow_redirects=True)
text_list = []
authors_list = []
for num_page in range(1, 20):
    response_new = work.get(f'https://quotes.toscrape.com/page/{num_page}/', headers=headers)
    soup_new = bs(response_new.text, 'lxml')
    res = soup_new.find_all('div', class_='quote')
    if res:
        print(num_page)

    if len(res) != 0:
        print('Enter into  if')
        for item_page in res:
            author_text_to_list = item_page.find('span', class_='text').text
            text_list.append(author_text_to_list)
            author_to_list = item_page.find('small', class_='author').text
            authors_list.append(author_to_list)

    else:
        break

for i in range(len(text_list)):
    print(text_list[i] + '\n' + authors_list[i] + '\n')
