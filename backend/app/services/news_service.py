from bs4 import BeautifulSoup
from models import NewsEntry
from utils import Constants, EntryParser, PageFetcher


class NewsService:
    def __init__(self, limit=Constants.MAX_NUMER_OF_ENTRIES):
        self.limit = limit
        self.fetcher = PageFetcher(Constants.HACKER_NEWS_URL)
        self.parser = EntryParser(self.limit)

    def fetch_hackernews_entries(self) -> list[NewsEntry]:
        try:
            response = self.fetcher.fetch_page()
            soup = BeautifulSoup(response.content, 'html.parser')
            entries = self.parser.parse_entries(soup)
            if not entries:
                raise ValueError("No entries found")
            return entries
        except (ValueError, ConnectionError, TimeoutError) as e:
            raise RuntimeError(f"Error fetching Hacker News entries: {str(e)}") from e

    def filter_entries_by_comments(self, entries: list[NewsEntry]) -> list[NewsEntry]:
        try:
            filtered = [
                entry for entry in entries
                if EntryParser.count_words(title=entry.title) > Constants.NUMBER_OF_WORDS
            ]
            return sorted(filtered, key=lambda x: x.comments, reverse=True)
        except AttributeError as e:
            raise ValueError(f"Invalid entry data: {str(e)}") from e

    def filter_entries_by_points(self, entries: list[NewsEntry]) -> list[NewsEntry]:
        try:
            filtered = [
                entry for entry in entries
                if EntryParser.count_words(title=entry.title) <= Constants.NUMBER_OF_WORDS
            ]
            return sorted(filtered, key=lambda x: x.points, reverse=True)
        except AttributeError as e:
            raise ValueError(f"Invalid entry data: {str(e)}") from e
