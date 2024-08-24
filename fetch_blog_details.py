import requests
from bs4 import BeautifulSoup

with open('blog_post_urls.txt', 'r') as f:
    blog_post_urls = f.read().splitlines()

blog_posts = []
for url in blog_post_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').text.strip()

    # Try to find OpenGraph image first
    image = soup.find('meta', property='og:image')
    if image:
        image_url = image['content']
    else:
        # If not found, use the first image in the post
        image = soup.find('img')
        image_url = image['src'] if image else None

    blog_posts.append((url, title, image_url))

with open('blog_posts.txt', 'w') as f:
    for url, title, image_url in blog_posts:
        f.write(f'{url}|{title}|{image_url}\n')
