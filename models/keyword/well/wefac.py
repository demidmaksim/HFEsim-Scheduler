from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WEFAC(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    ServiceFactor: float = Field(
        title="Коэффициент эксплуатации",
    )
    HZFactor: Optional[str] = Field(
        title="Учет в расчете потоков ветвей и расширенной сети",
    )


class WEFACSheet(KeywordsSheet):
    pass
