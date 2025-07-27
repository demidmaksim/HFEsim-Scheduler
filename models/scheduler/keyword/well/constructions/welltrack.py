from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class WELLTRACK(Keyword):
    WellName: Optional[str] = Field(
        alias="Имя скважины",
    )
    BoreName: Optional[int] = Field(
        alias="Номер ствола",
    )
    PointNumber: Optional[int] = Field(
        alias="Порядковый номер точки",
    )
    X: Optional[float] = Field(
        alias="X",
    )
    Y: Optional[float] = Field(
        alias="Y",
    )
    Z: Optional[float] = Field(
        alias="Z",
    )


class WELLTRACKSheet(KeywordsSheet):
    keyword = WELLTRACK
