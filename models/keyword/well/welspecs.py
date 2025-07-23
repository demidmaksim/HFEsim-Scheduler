from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class WELSPECS(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    GroupName: Optional[str] = Field(
        title="Группа скважины",
    )
    IW: Optional[float] = Field(
        title="IW",
    )
    JW: Optional[int] = Field(
        title="JW",
    )
    ReferenceDepth: Optional[int] = Field(
        title="Опорная глубина для забойного давления",
    )
    PreferredPhase: Optional[str] = Field(
        title="Предпочтительная фаза",
    )
    DrainageRadius: Optional[float] = Field(
        title="Радиус дренирования",
    )
    SpecialInflowEquation: Optional[str] = Field(
        title="Cпециальноe уравнениe притока",
    )
    AutomaticClosing: Optional[str] = Field(
        title="Aвтоматическое закрытие",
    )
    BilateralFlows: Optional[str] = Field(
        title="Возможность двусторонних перетоков",
    )
    PressureTable: Optional[int] = Field(
        title="Номер таблицы свойств в стволе скважины",
    )
    CalculatingDensity: Optional[str] = Field(
        title="Метод вычисления гидростатического напора",
    )
    PressureCalculationMethod: Optional[str] = Field(
        title="Способ расчета дебита в пластовых условиях"
    )


class WELSPECSSheet(KeywordsSheet):
    pass
