from pydantic import BaseModel


class NewsEntry(BaseModel):
    number: int
    title: str
    points: int
    comments: int
