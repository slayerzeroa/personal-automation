# get cnn news contents using beautifulsoup

import requests
from bs4 import BeautifulSoup as BS
from summarizer import Summarizer


# Summary
def get_summary(text):
    summarizer = Summarizer()
    summary = summarizer(text, min_length=100, max_length=800)  # You can adjust the min_length and max_length parameters
    return summary


# CNN Business Headline News
def get_cnn_news():
    link_list = []
    link_title = {}
    
    main_url = 'https://edition.cnn.com/business'
    req = requests.get(main_url)
    html = req.text

    soup = BS(html, 'html.parser')
    tags = soup.select('.stack')[0].find_all('a')
    for tag in tags:
        link_list.append('https://edition.cnn.com' + tag['href'])
        link_title[tag['href']] = tag.text  # 링크-타이틀 매칭
    
    headline_link = link_list[0]

    webpage = requests.get(headline_link)  # web
    soup = BS(webpage.content, "html.parser")

    # CNN 본문내용 html class
    data = soup.find_all(class_= "zn-body__paragraph")
    data_text_all = ""

    title = soup.find("h1", class_="pg-headline")

    if title == None:
        print('using requests is failed. \n try 2nd')
        data = soup.find_all(class_="paragraph inline-placeholder")
        data_text_all = ""
        title = soup.find("h1", class_="headline__text inline-placeholder")

    title_text = title.get_text()
    title_text = title_text.lstrip()
    # html 데이터에서 본문 텍스트만 뽑아오기
    for data_text in data:
      data_text = data_text.get_text()
      data_text_all = data_text_all + data_text

    return title_text, data_text_all, headline_link


