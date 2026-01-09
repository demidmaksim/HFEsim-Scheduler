from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WECONINJ(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    LowerEconomic: float = Field(
        alias="Нижний экономический предел объема закачки",
    )


class WECONINJSheet(KeywordsSheet):
    keyword = WECONINJ
