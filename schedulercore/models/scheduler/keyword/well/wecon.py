from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WECON(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    LowerOilRate: Optional[float] = Field(
        alias="Нижний экономический предел по дебиту нефти",
    )
    LowerGasRate: Optional[float] = Field(
        alias="Нижний экономический предел по дебиту газа",
    )
    UpperWCT: Optional[float] = Field(
        alias="Верхний экономический предел по обводненности",
    )
    UpperGOR: Optional[float] = Field(
        alias="Верхний экономический предел по газовому фактору",
    )
    UpperWaterInGas: Optional[float] = Field(
        alias="Верхний экономический предел по содержанию воды в газе"
    )
    WCTOperation: Optional[str] = Field(
        alias="Выполняемая операция при превышении предела обводненности"
    )
    EndCalculation: Optional[str] = Field(
        alias="Флаг, задающий конец расчета модели",
    )
    OpenWell: Optional[str] = Field(
        alias="Имя замещающей скважины",
    )
    EconLimitation: Optional[str] = Field(
        alias="Показатель минимального экономического ограничения"
    )
    WCTLimitation: Optional[float] = Field(
        alias="Вторичное ограничение по максимальной обводненности"
    )
    WCTLimitationOperation: Optional[str] = Field(
        alias="Операция при превышении вторичного ограничения обводненности"
    )
    UpperGasInLiquid: Optional[float] = Field(
        alias="Верхний предел по содержанию газа в жидкости",
    )
    LowerLiqud: Optional[float] = Field(
        alias="Нижний экономический предел по дебиту жидкости",
    )


class WECONSheet(KeywordsSheet):
    keyword = WECON
