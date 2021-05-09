import requests
from bs4 import BeautifulSoup

main_data = []

def request(url):
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text

def get_html(html):
    soup = BeautifulSoup(html, 'lxml')
    all_news = soup.find_all('div', class_="Tag--article")[:15]
    for news in all_news:
        news_title = news.find('a', class_="ArticleItem--name").text
    
        try:
            photo = news.find('img', class_="ArticleItem--image-img").get('data-src')
        except:
            photo = 'there is no photo'

        link = news.find('a', class_="ArticleItem--name").get('href')

        data = dict()
        data = {'news': news_title, 'photo': photo, 'link': link}
        main_data.append(data)

def main():
    link = 'https://kaktus.media/?lable=8&date=2021-03-05&order=popular'
    get_html(request(link))