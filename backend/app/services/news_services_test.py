from unittest.mock import Mock, patch

import pytest
from models import NewsEntry
from services import NewsService
from utils import EntryParser, PageFetcher

@pytest.fixture
def mock_page_fetcher():
    return Mock(spec=PageFetcher)

@pytest.fixture
def mock_entry_parser():
    return Mock(spec=EntryParser)

@pytest.fixture
def news_service(mock_page_fetcher, mock_entry_parser):
    service = NewsService()
    service.fetcher = mock_page_fetcher
    service.parser = mock_entry_parser
    return service

def test__fetch_hackernews_entries__returns_entries__when_they_are_found(news_service, mock_page_fetcher, mock_entry_parser):
    mock_response = Mock()
    mock_response.content = '<html><body><div class="entry"></div></body></html>'
    mock_page_fetcher.fetch_page.return_value = mock_response
    
    mock_entry_parser.parse_entries.return_value = [NewsEntry(title="Test Title", comments=10, points=5, number=1)]

    entries = news_service.fetch_hackernews_entries()

    assert len(entries) == 1
    assert entries[0].title == "Test Title"
    mock_page_fetcher.fetch_page.assert_called_once()
    mock_entry_parser.parse_entries.assert_called_once()

def test__fetch_hackernews_entries__raises_error__when_no_entries_are_found(news_service, mock_page_fetcher, mock_entry_parser):
    mock_response = Mock()
    mock_response.content = '<html><body></body></html>'
    mock_page_fetcher.fetch_page.return_value = mock_response
    
    mock_entry_parser.parse_entries.return_value = []

    with pytest.raises(RuntimeError, match="No entries found"):
        news_service.fetch_hackernews_entries()

def test__filter_entries_by_comments__returns_sorted_entries__when_they_are_found(news_service):
    entries = [
        NewsEntry(title="Short Title", comments=5, points=10, number=1),
        NewsEntry(title="Long Title with Many Words Test", comments=10, points=5, number=2)
    ]
    
    with patch.object(EntryParser, 'count_words', return_value=6):
        filtered_entries = news_service.filter_entries_by_comments(entries)
    
    assert len(filtered_entries) == 2
    assert filtered_entries[0].title == "Long Title with Many Words Test"
    assert filtered_entries[0].comments == 10

def test__filter_entries_by_points__returns_sorted_entries__when_they_are_found(news_service):
    entries = [
        NewsEntry(title="Short Title", comments=5, points=10, number=1),
        NewsEntry(title="Long Title with Many Words", comments=10, points=20, number=2)
    ]
    
    with patch.object(EntryParser, 'count_words', return_value=4):
        filtered_entries = news_service.filter_entries_by_points(entries)
    
    assert len(filtered_entries) == 2
    assert filtered_entries[0].title == "Long Title with Many Words"
    assert filtered_entries[0].points == 20

def test__filter_entries__raises_error__when_invalid_entry_data(news_service):
    entries = [Mock(title=None, comments=None, points=None, number=None)]
    
    with pytest.raises(ValueError) as excinfo:
        news_service.filter_entries_by_comments(entries)
    assert "Error counting words in" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        news_service.filter_entries_by_points(entries)
    assert "Error counting words in" in str(excinfo.value)
