from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WLIST(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    ListName: str = Field(
        title="Имя списка",
    )
    ListValue: Optional[str] = Field(
        title="Значение в списке",
    )


class WLISTSheet(KeywordsSheet):
    pass
