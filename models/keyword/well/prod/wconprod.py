from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WCONPROD(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    OperatingModes: str = Field(
        title="Режимы работы",
    )
    WellControl: str = Field(
        title="Управление скважиной",
    )
    OilFlowRate: Optional[float] = Field(
        title="Дебит нефти",
    )
    WaterFlowRate: Optional[float] = Field(
        title="Дебит воды",
    )
    GasFlowRate: Optional[float] = Field(
        title="Дебит газа",
    )
    LiquidFlowRate: Optional[float] = Field(
        title="Дебит жидкости",
    )
    FlowInReservoir: Optional[float] = Field(
        title="Дебит флюида в пластовых условиях",
    )
    BHP: Optional[float] = Field(
        title="Забойное давление",
    )
    THP: Optional[float] = Field(
        title="Устьевое давление",
    )
    VFP: Optional[int] = Field(
        title="Номер таблицы VFP",
    )
    ALQ: Optional[float] = Field(
        title="Величина ALQ",
    )
    WetGasRate: Optional[float] = Field(
        title="Дебит жирного газа",
    )
    MolarFlowRate: Optional[float] = Field(
        title="Молярный дебит",
    )
    SteamRate: Optional[float] = Field(
        title="Дебит пара",
    )
    PressureShift: Optional[float] = Field(
        title="Сдвиг давления",
    )
    TemperatureShift: Optional[float] = Field(
        title="Сдвиг температуры",
    )
    ThermalFlowRate: Optional[float] = Field(
        title="Тепловой дебит",
    )
    LinearCombination: Optional[float] = Field(
        title="Линейная комбинация",
    )
    NGLProduction: Optional[float] = Field(
        title="Дебит ШФЛУ",
    )


class WCONPRODSheet(KeywordsSheet):
    pass
