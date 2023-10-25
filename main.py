import requests
import os
from bs4 import BeautifulSoup

def simplify_dom(url: str) -> str:
    response = requests.get(url=url, timeout=30)

    if response.status_code != 200:
        raise Exception("Verify the URL")

    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted tags
    unwanted_tags = [
        'script', 'meta', 'link', 'style', 'noscript', 'base', 'source', 'track', 'path', 'svg'
    ]
    for tag in unwanted_tags:
        [t.extract() for t in soup.find_all(tag)]

    # Mapping by role
    for elem in soup.find_all(['textarea', 'input']):
        elem.name = 'i'
        elem.attrs = {'type': 'input'}

    for elem in soup.find_all(['div', 'section', 'article', 'main', 'nav', 'header', 'footer']):
        elem.name = 'c'

    for elem in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']):
        elem.name = 't'

    for elem in soup.find_all('a'):
        if 'href' in elem.attrs:
            elem.name = 'l'

    for elem in soup.find_all('button'):
        elem.name = 'b'

    for elem in soup.find_all(['img', 'video']):
        elem.name = 'm'

    useful_attrs = ['href', 'src', 'alt', 'title', 'role', 'aria-*']

    # Remove non-useful attributes from remaining elements
    for tag in soup.find_all(True):  # Iterating over all tags
        attrs = list(tag.attrs)
        for attr in attrs:
            if attr not in useful_attrs:
                del tag.attrs[attr]

    return str(soup)


def write_to_file(data: str):
    with open("output.txt", "a+") as f:
        f.write(data)
        f.close()


if __name__ == "__main__":
    URL = "https://www.github.com"
    simplified_dom = simplify_dom(URL)
    write_to_file(simplified_dom)