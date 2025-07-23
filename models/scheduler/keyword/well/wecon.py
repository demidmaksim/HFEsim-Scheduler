from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class WECON(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    LowerOilRate: Optional[float] = Field(
        title="Нижний экономический предел по дебиту нефти",
    )
    LowerGasRate: Optional[float] = Field(
        title="Нижний экономический предел по дебиту газа",
    )
    UpperWCT: Optional[float] = Field(
        title="Верхний экономический предел по обводненности",
    )
    UpperGOR: Optional[float] = Field(
        title="Верхний экономический предел по газовому фактору",
    )
    UpperWaterInGas: Optional[float] = Field(
        title="Верхний экономический предел по содержанию воды в газе"
    )
    WCTOperation: Optional[str] = Field(
        title="Выполняемая операция при превышении предела обводненности"
    )
    EndCalculation: Optional[str] = Field(
        title="Флаг, задающий конец расчета модели",
    )
    OpenWell: Optional[str] = Field(
        title="Имя замещающей скважины",
    )
    EconLimitation: Optional[str] = Field(
        title="Показатель минимального экономического ограничения"
    )
    WCTLimitation: Optional[float] = Field(
        title="Вторичное ограничение по максимальной обводненности"
    )
    WCTLimitationOperation: Optional[str] = Field(
        title="Операция при превышении вторичного ограничения обводненности"
    )
    UpperGasInLiquid: Optional[float] = Field(
        title="Верхний предел по содержанию газа в жидкости",
    )
    LowerLiqud: Optional[float] = Field(
        title="Нижний экономический предел по дебиту жидкости",
    )


class WECONSheet(KeywordsSheet):
    keyword = WECON
