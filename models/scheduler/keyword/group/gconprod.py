from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class GCONPROD(Keyword):
    GroupName: str = Field(
        title="Имя группы",
    )
    ControlType: str = Field(
        title="Тип контроля",
    )
    OilRate: Optional[float] = Field(
        title="Дебит нефти",
    )
    WaterRate: Optional[float] = Field(
        title="Дебит воды",
    )
    GasRate: Optional[float] = Field(
        title="Дебит газа",
    )
    LiquidRate: Optional[float] = Field(
        title="Дебит жидкости",
    )
    LimitOpertion: Optional[str] = Field(
        title="Выполняемая операция при превышении",
    )
    GroupToGroup: Optional[str] = Field(
        title="Может ли дебит группы контролироваться группой",
    )
    DirectionalRate: Optional[float] = Field(
        title="Направляющий дебит группы",
    )
    Phase: Optional[str] = Field(
        title="Фаза, для которой применяется предыдущий параметр",
    )
    WatLimitOperation: Optional[str] = Field(
        title="Операция при превышении ограничения на дебит воды"
    )
    GasLimitOperation: Optional[str] = Field(
        title="Операция при превышении ограничения на дебит газа"
    )
    LiqLimitOperation: Optional[str] = Field(
        title="Операция при превышении ограничения на дебит жидкости"
    )
    FluidInReservoir: Optional[float] = Field(
        title="Дебит флюида в пластовых условиях",
    )
    BalancingProportion: Optional[float] = Field(
        title="Значение уравновешивающей доли отбора.",
    )
    WetGasRate: Optional[float] = Field(
        title="Дебит жирного газа",
    )
    HeatFlow: Optional[float] = Field(
        title="Заданный дебит теплоты",
    )
    GasInPlace: Optional[float] = Field(
        title="Доля дебита газа в поверхностных условиях",
    )
    WaterInPlace: Optional[float] = Field(
        title="Доля дебита воды в поверхностных условиях",
    )


class GCONPRODSheet(KeywordsSheet):
    keyword = GCONPROD
