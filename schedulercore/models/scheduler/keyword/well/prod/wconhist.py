from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WCONHIST(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    OperatingModes: str = Field(
        alias="Режимы работы",
    )
    WellControl: str = Field(
        alias="Управление скважиной",
    )
    OilFlowRate: float = Field(
        alias="Дебит нефти",
    )
    WaterFlowRate: float = Field(
        alias="Дебит воды",
    )
    GasFlowRate: float = Field(
        alias="Дебит газа",
    )
    VFP: Optional[int] = Field(
        alias="Номер таблицы VFP",
    )
    ALQ: Optional[float] = Field(
        alias="Величина ALQ",
    )
    THP: Optional[float] = Field(
        alias="Устьевое давление",
    )
    BHP: Optional[float] = Field(
        alias="Забойное давление",
    )
    WetGasRate: Optional[float] = Field(
        alias="Дебит жирного газа",
    )
    NGLProduction: Optional[float] = Field(
        alias="Дебит ШФЛУ",
    )


class WCONHISTSheet(KeywordsSheet):
    keyword = WCONHIST
