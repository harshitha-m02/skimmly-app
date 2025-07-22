from bs4 import BeautifulSoup
import requests


def fetch_url_text(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.get_text()