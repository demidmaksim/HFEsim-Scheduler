from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class COMPDATMD(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    Bore: Optional[int] = Field(
        alias="Номер ствола",
    )
    FirstCutoff: Optional[float] = Field(
        alias="Первая отсечка перфорации",
    )
    UpperLimit: Optional[float] = Field(
        alias="Верхний предел перфорации",
    )
    DepthID: Optional[str] = Field(
        alias="Идентификатор значения глубины перфорации",
    )
    PerforationStatus: Optional[str] = Field(
        alias="Статус перфорации",
    )
    SaturationTable: Optional[int] = Field(
        alias="Номер таблицы насыщенности",
    )
    ConductivityCoefficient: Optional[float] = Field(
        alias="Коэффициент проводимости",
    )
    BoreholeDiameter: Optional[float] = Field(
        alias="Диаметр скважины",
    )
    KH: Optional[float] = Field(
        alias="Величина KH",
    )
    SKIN: Optional[float] = Field(
        alias="Cкин",
    )
    DFactor: Optional[float] = Field(
        alias="D-фактор",
    )
    ConductivityMultiplier: Optional[float] = Field(
        alias="Множитель коэффициента проводимости",
    )
    PerforationType: Optional[str] = Field(
        alias="Тип перфорации",
    )
    AutopsyNumber: Optional[int] = Field(
        alias="Номер вскрытия",
    )


class COMPDATMDSheet(KeywordsSheet):
    keyword = COMPDATMD
