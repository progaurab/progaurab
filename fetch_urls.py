import requests
from bs4 import BeautifulSoup

sitemap_url = 'https://www.instilllearning.com/sitemap.xml'
response = requests.get(sitemap_url)
soup = BeautifulSoup(response.content, 'xml')

urls = [url.text for url in soup.find_all('loc')]
blog_post_urls = [url for url in urls if '/blog/' in url][:10]

with open('blog_post_urls.txt', 'w') as f:
    for url in blog_post_urls:
        f.write(url + '\n')
