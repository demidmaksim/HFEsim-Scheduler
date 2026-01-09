from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WEFAC(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    ServiceFactor: float = Field(
        alias="Коэффициент эксплуатации",
    )
    HZFactor: Optional[str] = Field(
        alias="Учет в расчете потоков ветвей и расширенной сети",
    )


class WEFACSheet(KeywordsSheet):
    keyword = WEFAC
