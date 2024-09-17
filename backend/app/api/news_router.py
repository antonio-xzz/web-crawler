from fastapi import APIRouter, HTTPException, Depends
from models import NewsEntry
from services import NewsService

router = APIRouter()

def fetch_and_filter(news_service: NewsService, filter_func=None):
    try:
        entries = news_service.fetch_hackernews_entries()
        if filter_func:
            return filter_func(entries)
        return entries
    except Exception:
        raise HTTPException(status_code=500, detail="Error processing request")


@router.get("/entries", response_model=list[NewsEntry])
def get_entries(news_service: NewsService = Depends(NewsService)):
    return fetch_and_filter(news_service)


@router.get("/entries/comments", response_model=list[NewsEntry])
def filter_by_comments(news_service: NewsService = Depends(NewsService)):
    return fetch_and_filter(news_service, news_service.filter_entries_by_comments)


@router.get("/entries/points", response_model=list[NewsEntry])
def filter_by_points(news_service: NewsService = Depends(NewsService)):
    return fetch_and_filter(news_service, news_service.filter_entries_by_points)
