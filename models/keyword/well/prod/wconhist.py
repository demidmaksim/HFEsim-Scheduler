from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WCONHIST(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    OperatingModes: str = Field(
        title="Режимы работы",
    )
    WellControl: str = Field(
        title="Управление скважиной",
    )
    OilFlowRate: float = Field(
        title="Дебит нефти",
    )
    WaterFlowRate: float = Field(
        title="Дебит воды",
    )
    GasFlowRate: float = Field(
        title="Дебит газа",
    )
    VFP: Optional[int] = Field(
        title="Номер таблицы VFP",
    )
    ALQ: Optional[float] = Field(
        title="Величина ALQ",
    )
    THP: Optional[float] = Field(
        title="Устьевое давление",
    )
    BHP: Optional[float] = Field(
        title="Забойное давление",
    )
    WetGasRate: Optional[float] = Field(
        title="Дебит жирного газа",
    )
    NGLProduction: Optional[float] = Field(
        title="Дебит ШФЛУ",
    )


class WCONHISTSheet(KeywordsSheet):
    keyword = WCONHIST
