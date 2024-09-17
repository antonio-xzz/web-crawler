from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from main import app
from models import NewsEntry
from services import NewsService

client = TestClient(app)

@pytest.fixture
def mock_news_service():
    return MagicMock(spec=NewsService)

@pytest.fixture
def sample_entries():
    return [
        NewsEntry(number=1, title="Test Entry 1", points=100, comments=50),
        NewsEntry(number=2, title="Test Entry 2", points=200, comments=150)
    ]

@pytest.fixture(autouse=True)
def override_dependency(mock_news_service):
    app.dependency_overrides[NewsService] = lambda: mock_news_service
    yield
    app.dependency_overrides = {}

def test__returns_all_entries__when_no_filter(mock_news_service, sample_entries):
    mock_news_service.fetch_hackernews_entries.return_value = sample_entries
    
    response = client.get("/entries")
    
    assert response.status_code == 200
    assert len(response.json()) == len(sample_entries)
    mock_news_service.fetch_hackernews_entries.assert_called_once()

def test__raises_500__when_fetch_fails(mock_news_service):
    mock_news_service.fetch_hackernews_entries.side_effect = Exception("Fetch error")
    
    response = client.get("/entries")
    
    assert response.status_code == 500
    assert response.json()["detail"] == "Error processing request"

def test__filters_entries_by_comments__when_called(mock_news_service, sample_entries):
    mock_news_service.fetch_hackernews_entries.return_value = sample_entries
    mock_news_service.filter_entries_by_comments.return_value = [sample_entries[1]]
    
    response = client.get("/entries/comments")
    
    assert response.status_code == 200
    assert len(response.json()) == 1
    mock_news_service.filter_entries_by_comments.assert_called_once()

def test__filters_entries_by_points__when_called(mock_news_service, sample_entries):
    mock_news_service.fetch_hackernews_entries.return_value = sample_entries
    mock_news_service.filter_entries_by_points.return_value = [sample_entries[0]]
    
    response = client.get("/entries/points")
    
    assert response.status_code == 200
    assert len(response.json()) == 1
    mock_news_service.filter_entries_by_points.assert_called_once()
