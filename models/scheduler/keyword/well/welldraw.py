from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class WELDRAW(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    MaxDrow: float = Field(
        title="Максимально допустимая депрессия",
    )
    Phase: Optional[str] = Field(
        title="Фаза",
    )
    DrowLimit: Optional[float] = Field(
        title="Учет ограничения депрессии при расчете потенциала добычи",
    )
    TypeLimit: Optional[str] = Field(
        title="Ограничивается ли взвешенное по индексу продуктивности PI",
    )


class WELDRAWSheet(KeywordsSheet):
    keyword = WELDRAW
