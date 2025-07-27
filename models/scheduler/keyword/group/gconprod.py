from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class GCONPROD(Keyword):
    GroupName: str = Field(
        alias="Имя группы",
    )
    ControlType: str = Field(
        alias="Тип контроля",
    )
    OilRate: Optional[float] = Field(
        alias="Дебит нефти",
    )
    WaterRate: Optional[float] = Field(
        alias="Дебит воды",
    )
    GasRate: Optional[float] = Field(
        alias="Дебит газа",
    )
    LiquidRate: Optional[float] = Field(
        alias="Дебит жидкости",
    )
    LimitOpertion: Optional[str] = Field(
        alias="Выполняемая операция при превышении",
    )
    GroupToGroup: Optional[str] = Field(
        alias="Может ли дебит группы контролироваться группой",
    )
    DirectionalRate: Optional[float] = Field(
        alias="Направляющий дебит группы",
    )
    Phase: Optional[str] = Field(
        alias="Фаза, для которой применяется предыдущий параметр",
    )
    WatLimitOperation: Optional[str] = Field(
        alias="Операция при превышении ограничения на дебит воды"
    )
    GasLimitOperation: Optional[str] = Field(
        alias="Операция при превышении ограничения на дебит газа"
    )
    LiqLimitOperation: Optional[str] = Field(
        alias="Операция при превышении ограничения на дебит жидкости"
    )
    FluidInReservoir: Optional[float] = Field(
        alias="Дебит флюида в пластовых условиях",
    )
    BalancingProportion: Optional[float] = Field(
        alias="Значение уравновешивающей доли отбора.",
    )
    WetGasRate: Optional[float] = Field(
        alias="Дебит жирного газа",
    )
    HeatFlow: Optional[float] = Field(
        alias="Заданный дебит теплоты",
    )
    GasInPlace: Optional[float] = Field(
        alias="Доля дебита газа в поверхностных условиях",
    )
    WaterInPlace: Optional[float] = Field(
        alias="Доля дебита воды в поверхностных условиях",
    )


class GCONPRODSheet(KeywordsSheet):
    keyword = GCONPROD
