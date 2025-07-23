from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class FRACTURE_SPECS(Keyword):
    WellName: str = Field(
        title="Имя скважины",
    )
    Bore: Optional[int] = Field(
        title="Ствол",
    )
    FracName: str = Field(
        title="Имя трещины",
    )
    MD: float = Field(
        title="MD",
    )
    Azimuth: Optional[float] = Field(
        title="Азимутальный угол",
    )
    Antiaircraft: Optional[float] = Field(
        title="Зенитный угол",
    )
    LeftHalfLength: float = Field(
        title="Левая полудлина",
    )
    RightHalfLength: float = Field(
        title="Правая полудлина",
    )
    Height1: float = Field(
        title="Высота трещины в первом направлении",
    )
    Height2: float = Field(
        title="Высота трещины во втором направлении",
    )
    Width: float = Field(
        title="Ширина трещины FZ",
    )
    CrackAffectedZoneWidth: Optional[float] = Field(
        title="Ширина зоны влияния трещины",
    )
    CrackBoundaryCurvature: Optional[float] = Field(
        title="Кривизна границы трещины",
    )
    ReservoirPermeabilityMultiplier: Optional[float] = Field(
        title="Множитель проницаемости пласта",
    )
    Permeability: Optional[float] = Field(
        title="Проницаемость",
    )
    CrackImpactPermeability: Optional[float] = Field(
        title="Проницаемость в зоне влияния трещины (NFZ)"
    )
    MatrixPermeability: Optional[float] = Field(
        title="Проницаемость трещины (Матрицы)",
    )
    CrackImpactPermeability2: Optional[float] = Field(
        title="Проницаемость в зоне влияния трещины (NFZ2)"
    )
    FractureProductivityMultiplier: Optional[float] = Field(
        title="Множитель продуктивности трещины"
    )
    ProppantTypeName: Optional[str] = Field(
        title="Название типа пропанта",
    )
    ProppantProperties: Optional[str] = Field(
        title="Xарактеристика падения проницаемости",
    )
    FallPeriod: Optional[float] = Field(
        title="Период падения проницаемости в трещине",
    )
    FlowModel: Optional[str] = Field(
        title="Имя функции зависимости проницаемости трещины от времени"
    )


class FRACTURE_SPECSSheet(KeywordsSheet):
    keyword = FRACTURE_SPECS
