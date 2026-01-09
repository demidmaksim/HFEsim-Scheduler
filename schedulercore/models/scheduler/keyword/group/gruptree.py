from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class GRUPTREE(Keyword):
    GroupName: str = Field(
        alias="Имя группы",
    )  # обязательное поле
    ParentGroup: Optional[str] = Field(
        alias="Родительская группа",
    )
    Description: Optional[str] = Field(
        alias="Описание",
    )


class GRUPTREESheet(KeywordsSheet):
    keyword = GRUPTREE
