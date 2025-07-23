from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WELLTRACK(Keyword):
    WellName: Optional[str] = Field(
        title="Имя скважины",
    )
    BoreName: Optional[int] = Field(
        title="Номер ствола",
    )
    PointNumber: Optional[int] = Field(
        title="Порядковый номер точки",
    )
    X: Optional[float] = Field(
        title="X",
    )
    Y: Optional[float] = Field(
        title="Y",
    )
    Z: Optional[float] = Field(
        title="Z",
    )


class WELLTRACKSheet(KeywordsSheet):
    pass
