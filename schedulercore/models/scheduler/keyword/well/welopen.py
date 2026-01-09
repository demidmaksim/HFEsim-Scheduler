from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WELOPEN(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    OpenDate: Optional[str] = Field(
        alias="Дата вскрытия",
    )
    OpenReason: Optional[str] = Field(
        alias="Причина вскрытия",
    )


class WELOPENSheet(KeywordsSheet):
    keyword = WELOPEN
