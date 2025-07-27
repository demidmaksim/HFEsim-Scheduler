from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class Comment(Keyword):
    Comment: Optional[str] = Field(
        alias="Комминтарий",
    )


class CommentSheet(KeywordsSheet):
    keyword = Comment
