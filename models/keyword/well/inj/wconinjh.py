from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WCONINJH(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    FluidType: str = Field(
        title="Тип закачиваемого флюида",
    )
    OperatingModes: str = Field(
        title="Режим работы скважины",
    )
    VolumeInPlace: Optional[float] = Field(
        title="Объем закачки в поверхностных условиях",
    )
    BHP: Optional[float] = Field(
        title="Забойное давление",
    )
    THP: Optional[float] = Field(
        title="Устьевое давление",
    )
    VFR: Optional[int] = Field(
        title="номер VFP",
    )
    OilInFluid: Optional[float] = Field(
        title="Концентрация нефти в нагнетаемом флюиде",
    )
    OilInRate: Optional[float] = Field(
        title="Доля нефти в потоке нагнетания",
    )
    WaterInRate: Optional[float] = Field(
        title="Доля воды в потоке нагнетания",
    )
    GasInRate: Optional[float] = Field(
        title="Доля газа в потоке нагнетания",
    )
    WellControl: str = Field(
        title="Режим контроля скважины:",
    )


class WCONINJHSheet(KeywordsSheet):
    keyword = WCONINJH
