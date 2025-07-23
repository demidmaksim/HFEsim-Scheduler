from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class WSEGVALV(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    Segment: int = Field(
        title="Номер сегмента",
    )
    FlowRateCoef: float = Field(
        title="Коэффициент расхода для клапана",
    )
    CrossSectionalAreaFlow: float = Field(
        title="Площадь поперечного сечения для потока",
    )
    AdditionalPipeLength: Optional[float] = Field(
        title="Дополнительная длина трубы",
    )
    PipeDiameter: Optional[float] = Field(
        title="Диаметр трубы",
    )
    AbsoluteRoughness: Optional[float] = Field(
        title="Абсолютная шероховатость",
    )
    CrossSectionalAreaPipe: Optional[float] = Field(
        title="Площадь поперечного сечения трубы",
    )
    Mode: Optional[str] = Field(
        title="Статус",
    )
    MaxCrossSectionalArea: Optional[float] = Field(
        title="Максимальная площадь поперечного сечения",
    )


class WSEGVALVheet(KeywordsSheet):
    keyword = WSEGVALV
