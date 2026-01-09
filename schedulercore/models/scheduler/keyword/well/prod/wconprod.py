from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WCONPROD(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    OperatingModes: str = Field(
        alias="Режимы работы",
    )
    WellControl: str = Field(
        alias="Управление скважиной",
    )
    OilFlowRate: Optional[float] = Field(
        alias="Дебит нефти",
    )
    WaterFlowRate: Optional[float] = Field(
        alias="Дебит воды",
    )
    GasFlowRate: Optional[float] = Field(
        alias="Дебит газа",
    )
    LiquidFlowRate: Optional[float] = Field(
        alias="Дебит жидкости",
    )
    FlowInReservoir: Optional[float] = Field(
        alias="Дебит флюида в пластовых условиях",
    )
    BHP: Optional[float] = Field(
        alias="Забойное давление",
    )
    THP: Optional[float] = Field(
        alias="Устьевое давление",
    )
    VFP: Optional[int] = Field(
        alias="Номер таблицы VFP",
    )
    ALQ: Optional[float] = Field(
        alias="Величина ALQ",
    )
    WetGasRate: Optional[float] = Field(
        alias="Дебит жирного газа",
    )
    MolarFlowRate: Optional[float] = Field(
        alias="Молярный дебит",
    )
    SteamRate: Optional[float] = Field(
        alias="Дебит пара",
    )
    PressureShift: Optional[float] = Field(
        alias="Сдвиг давления",
    )
    TemperatureShift: Optional[float] = Field(
        alias="Сдвиг температуры",
    )
    ThermalFlowRate: Optional[float] = Field(
        alias="Тепловой дебит",
    )
    LinearCombination: Optional[float] = Field(
        alias="Линейная комбинация",
    )
    NGLProduction: Optional[float] = Field(
        alias="Дебит ШФЛУ",
    )


class WCONPRODSheet(KeywordsSheet):
    keyword = WCONPROD
