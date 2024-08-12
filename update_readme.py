import re

with open('blog_posts.txt', 'r') as f:
    blog_posts = [line.split('|') for line in f.read().splitlines()][:10]

with open('README.md', 'r') as f:
    readme_content = f.read()

new_blog_posts_section = "## Recent Blog Posts\n\n"
for url, title, image_url in blog_posts:
    if image_url:
        new_blog_posts_section += f'<a href="{url}"><img src="{image_url}" alt="{title}" width="100" align="left" hspace="10" vspace="10"></a>'  # Decreased width to 100 (50% of 200)
    new_blog_posts_section += f"<p>**[{title}]({url})**</p>\n<br>"

updated_readme_content = re.sub(r'## Recent Blog Posts.*', new_blog_posts_section, readme_content, flags=re.DOTALL)

with open('README.md', 'w') as f:
    f.write(updated_readme_content)
