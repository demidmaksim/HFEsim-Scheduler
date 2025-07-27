from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class WELSPECS(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    GroupName: Optional[str] = Field(
        alias="Группа скважины",
    )
    IW: Optional[float] = Field(
        alias="IW",
    )
    JW: Optional[int] = Field(
        alias="JW",
    )
    ReferenceDepth: Optional[int] = Field(
        alias="Опорная глубина для забойного давления",
    )
    PreferredPhase: Optional[str] = Field(
        alias="Предпочтительная фаза",
    )
    DrainageRadius: Optional[float] = Field(
        alias="Радиус дренирования",
    )
    SpecialInflowEquation: Optional[str] = Field(
        alias="Cпециальноe уравнениe притока",
    )
    AutomaticClosing: Optional[str] = Field(
        alias="Aвтоматическое закрытие",
    )
    BilateralFlows: Optional[str] = Field(
        alias="Возможность двусторонних перетоков",
    )
    PressureTable: Optional[int] = Field(
        alias="Номер таблицы свойств в стволе скважины",
    )
    CalculatingDensity: Optional[str] = Field(
        alias="Метод вычисления гидростатического напора",
    )
    PressureCalculationMethod: Optional[str] = Field(
        alias="Способ расчета дебита в пластовых условиях"
    )


class WELSPECSSheet(KeywordsSheet):
    keyword = WELSPECS
