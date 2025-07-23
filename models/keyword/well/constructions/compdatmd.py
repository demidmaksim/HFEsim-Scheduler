from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class COMPDATMD(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    Bore: Optional[int] = Field(
        title="Номер ствола",
    )
    FirstCutoff: Optional[float] = Field(
        title="Первая отсечка перфорации",
    )
    UpperLimit: Optional[float] = Field(
        title="Верхний предел перфорации",
    )
    DepthID: Optional[str] = Field(
        title="Идентификатор значения глубины перфорации",
    )
    PerforationStatus: Optional[str] = Field(
        title="Статус перфорации",
    )
    SaturationTable: Optional[int] = Field(
        title="Номер таблицы насыщенности",
    )
    ConductivityCoefficient: Optional[float] = Field(
        title="Коэффициент проводимости",
    )
    BoreholeDiameter: Optional[float] = Field(
        title="Диаметр скважины",
    )
    KH: Optional[float] = Field(
        title="Величина KH",
    )
    SKIN: Optional[float] = Field(
        title="Cкин",
    )
    DFactor: Optional[float] = Field(
        title="D-фактор",
    )
    ConductivityMultiplier: Optional[float] = Field(
        title="Множитель коэффициента проводимости",
    )
    PerforationType: Optional[str] = Field(
        title="Тип перфорации",
    )
    AutopsyNumber: Optional[int] = Field(
        title="Номер вскрытия",
    )


class COMPDATMDSheet(KeywordsSheet):
    keyword = COMPDATMD
