from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class GCONINJE(Keyword):
    GroupName: str = Field(
        alias="Имя группы",
    )
    FluidType: str = Field(
        alias="Тип закачиваемого флюида",
    )
    ControlType: str = Field(
        alias="Тип контроля",
    )
    VolumeInPlace: Optional[float] = Field(
        alias="Объем закачки в поверхностных условиях",
    )
    VolumeInReservoir: Optional[float] = Field(
        alias="Объем закачки в пластовых условиях",
    )
    TargetReInjection: Optional[float] = Field(
        alias="Целевой коэффициент повторной закачки",
    )
    TargetCompensationFactor: Optional[float] = Field(
        alias="Целевой коэффициент компенсации",
    )
    GroupToGroup: Optional[str] = Field(
        alias="Может ли дебит группы контролироваться группой",
    )
    DirectionalRate: Optional[float] = Field(
        alias="Направляющий дебит группы",
    )
    DirectionalRateType: Optional[str] = Field(
        alias="Тип направляющего дебита для предыдущего параметра"
    )
    GroupNameForBack: Optional[str] = Field(
        alias="Имя группы для контроля доли дебита для ре-закачки"
    )
    GroupNameForReplac: Optional[str] = Field(
        alias="Имя группы для контроля доли отбора для ре-закачки"
    )


class GCONINJESheet(KeywordsSheet):
    keyword = GCONINJE
