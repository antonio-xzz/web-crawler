import re

import requests
from bs4 import BeautifulSoup
from models import NewsEntry


class Constants:
    HACKER_NEWS_URL: str = 'https://news.ycombinator.com/'
    NUMBER_OF_WORDS: int = 5
    MAX_NUMER_OF_ENTRIES: int = 30

class PageFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            raise ConnectionError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            raise ConnectionError(f"Error fetching page: {err}")

class EntryParser:
    def __init__(self, limit: int):
        self.limit = limit

    def parse_entries(self, soup: BeautifulSoup) -> list[NewsEntry]:
        try:
            entries = []
            items = soup.select('.athing')[:self.limit]

            for item in items:
                number_element = item.select_one('.rank')
                number = number_element.get_text().strip('.') if number_element else 'No number'

                title_element = item.select_one('.titleline > a')
                title = title_element.get_text() if title_element else 'No title'

                subtext = item.find_next_sibling('tr').select_one('.subtext')
                points_element = subtext.select_one('.score') if subtext else None
                points = points_element.get_text().split()[0] if points_element else '0'

                comments_element = subtext.select('a')[-1] if subtext and len(subtext.select('a')) > 0 else None
                comments = comments_element.get_text().split()[0] if comments_element and comments_element.get_text() != 'discuss' else '0'

                if number and title:
                    entries.append(NewsEntry(
                        number=int(number),
                        title=title,
                        points=int(points) if points.isdigit() else 0,
                        comments=int(comments) if comments.isdigit() else 0,
                    ))

            return entries
        except (AttributeError, ValueError) as e:
            raise ValueError(f"Error parsing entries: {e}")

    @staticmethod
    def count_words(title: str) -> int:
        try:
            words = re.sub(r'[^\w\s]', '', title).split()
            return len(words)
        except Exception as e:
            raise ValueError(f"Error counting words in title '{title}': {e}")
