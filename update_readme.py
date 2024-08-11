import re

with open('blog_posts.txt', 'r') as f:
    blog_posts = [line.split('|') for line in f.read().splitlines()]

with open('README.md', 'r') as f:
    readme_content = f.read()

new_blog_posts_section = "## Recent Blog Posts\n\n"
for url, title, image_url in blog_posts:
    if image_url:
        new_blog_posts_section += f'<a href="{url}"><img src="{image_url}" alt="{title}" width="200" align="left" hspace="10" vspace="10"></a>'
    new_blog_posts_section += f"[{title}]({url})\n\n"

updated_readme_content = re.sub(r'## Recent Blog Posts.*', new_blog_posts_section, readme_content, flags=re.DOTALL)

with open('README.md', 'w') as f:
    f.write(updated_readme_content)
