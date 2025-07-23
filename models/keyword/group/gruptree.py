from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class GRUPTREE(Keyword):
    GroupName: str = Field(
        title="Имя группы",
    )  # обязательное поле
    ParentGroup: Optional[str] = Field(
        title="Родительская группа",
    )
    Description: Optional[str] = Field(
        title="Описание",
    )


class GRUPTREESheet(KeywordsSheet):
    keyword = GRUPTREE
