from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WLIST(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    ListName: str = Field(
        alias="Имя списка",
    )
    ListValue: Optional[str] = Field(
        alias="Значение в списке",
    )


class WLISTSheet(KeywordsSheet):
    keyword = WLIST
