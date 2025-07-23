from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class GCONINJE(Keyword):
    GroupName: str = Field(
        title="Имя группы",
    )
    FluidType: str = Field(
        title="Тип закачиваемого флюида",
    )
    ControlType: str = Field(
        title="Тип контроля",
    )
    VolumeInPlace: Optional[float] = Field(
        title="Объем закачки в поверхностных условиях",
    )
    VolumeInReservoir: Optional[float] = Field(
        title="Объем закачки в пластовых условиях",
    )
    TargetReInjection: Optional[float] = Field(
        title="Целевой коэффициент повторной закачки",
    )
    TargetCompensationFactor: Optional[float] = Field(
        title="Целевой коэффициент компенсации",
    )
    GroupToGroup: Optional[str] = Field(
        title="Может ли дебит группы контролироваться группой",
    )
    DirectionalRate: Optional[float] = Field(
        title="Направляющий дебит группы",
    )
    DirectionalRateType: Optional[str] = Field(
        title="Тип направляющего дебита для предыдущего параметра"
    )
    GroupNameForBack: Optional[str] = Field(
        title="Имя группы для контроля доли дебита для ре-закачки"
    )
    GroupNameForReplac: Optional[str] = Field(
        title="Имя группы для контроля доли отбора для ре-закачки"
    )


class GCONINJESheet(KeywordsSheet):
    pass
