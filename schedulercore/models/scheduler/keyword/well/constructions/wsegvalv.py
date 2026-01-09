from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class WSEGVALV(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    Segment: int = Field(
        alias="Номер сегмента",
    )
    FlowRateCoef: float = Field(
        alias="Коэффициент расхода для клапана",
    )
    CrossSectionalAreaFlow: float = Field(
        alias="Площадь поперечного сечения для потока",
    )
    AdditionalPipeLength: Optional[float] = Field(
        alias="Дополнительная длина трубы",
    )
    PipeDiameter: Optional[float] = Field(
        alias="Диаметр трубы",
    )
    AbsoluteRoughness: Optional[float] = Field(
        alias="Абсолютная шероховатость",
    )
    CrossSectionalAreaPipe: Optional[float] = Field(
        alias="Площадь поперечного сечения трубы",
    )
    Mode: Optional[str] = Field(
        alias="Статус",
    )
    MaxCrossSectionalArea: Optional[float] = Field(
        alias="Максимальная площадь поперечного сечения",
    )


class WSEGVALVheet(KeywordsSheet):
    keyword = WSEGVALV
