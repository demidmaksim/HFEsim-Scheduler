from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WCONINJE(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    FluidType: str = Field(
        alias="Тип закачиваемого флюида",
    )
    OperatingModes: str = Field(
        alias="Режим работы скважины",
    )
    WellControl: str = Field(
        alias="Управление скважиной",
    )
    VolumeInPlace: Optional[float] = Field(
        alias="Объем закачки в поверхностных условиях",
    )
    VolumeInReservoir: Optional[float] = Field(
        alias="Объем закачки в пластовых условиях",
    )
    BHP: Optional[float] = Field(
        alias="Забойное давление",
    )
    THP: Optional[float] = Field(
        alias="Устьевое давление",
    )
    VFR: Optional[int] = Field(
        alias="номер VFP",
    )
    OilInFluid: Optional[float] = Field(
        alias="Концентрация нефти в нагнетаемом флюиде",
    )
    OilInRate: Optional[float] = Field(
        alias="Доля нефти в потоке нагнетания",
    )
    WaterInRate: Optional[float] = Field(
        alias="Доля воды в потоке нагнетания",
    )
    GasInRate: Optional[float] = Field(
        alias="Доля газа в потоке нагнетания",
    )


class WCONINJESheet(KeywordsSheet):
    keyword = WCONINJE
