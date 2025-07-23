from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WELOPEN(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    OpenDate: Optional[str] = Field(
        title="Дата вскрытия",
    )
    OpenReason: Optional[str] = Field(
        title="Причина вскрытия",
    )


class WELOPENSheet(KeywordsSheet):
    pass
