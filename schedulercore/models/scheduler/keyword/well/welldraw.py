from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WELDRAW(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    MaxDrow: float = Field(
        alias="Максимально допустимая депрессия",
    )
    Phase: Optional[str] = Field(
        alias="Фаза",
    )
    DrowLimit: Optional[float] = Field(
        alias="Учет ограничения депрессии при расчете потенциала добычи",
    )
    TypeLimit: Optional[str] = Field(
        alias="Ограничивается ли взвешенное по индексу продуктивности PI",
    )


class WELDRAWSheet(KeywordsSheet):
    keyword = WELDRAW
