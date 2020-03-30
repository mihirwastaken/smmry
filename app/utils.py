import time

import requests
from newspaper import Article

from app import app
from app import sumbasic

NEWSAPI_BASE_URL = 'https://newsapi.org/v2/'

def get_news_urls(query):
    headers = {
        'X-API-Key': app.config['NEWSAPIKEY']
    }
    payload = {
        'q': query,
        'pageSize': '5',
        'language': 'en',
    }
    result = requests.get(NEWSAPI_BASE_URL + 'everything', headers=headers, params=payload).json()
    return [article['url'] for article in result['articles']]

def get_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
    except:
        print('Failed to fetch article from', url)
        text = ''
    return text

def get_summary(query):
    word_limit = 300
    tic = time.perf_counter()
    print(f'\nQuery: \'{query}\', Word Limit: {word_limit}')
    print('Fetching Article URLS...', end=' ')
    urls = get_news_urls(query)
    print('Done ✔')
    print('Extracting Article Text...', end=' ')
    lines = [get_article_text(url) for url in urls]
    print('Done ✔')
    print('Summarizing...', end=' ')
    summary = sumbasic.orig(lines, word_limit)
    print('Done ✔')
    toc = time.perf_counter()
    tc = f'{toc - tic:0.3f}'
    print(f'Completed in {tc} seconds')
    return summary, urls, word_limit, tc