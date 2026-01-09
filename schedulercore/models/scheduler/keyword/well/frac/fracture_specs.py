from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class FRACTURE_SPECS(Keyword):
    WellName: str = Field(
        alias="Имя скважины",
    )
    Bore: Optional[int] = Field(
        alias="Ствол",
    )
    FracName: str = Field(
        alias="Имя трещины",
    )
    MD: float = Field(
        alias="MD",
    )
    Azimuth: Optional[float] = Field(
        alias="Азимутальный угол",
    )
    Antiaircraft: Optional[float] = Field(
        alias="Зенитный угол",
    )
    LeftHalfLength: float = Field(
        alias="Левая полудлина",
    )
    RightHalfLength: float = Field(
        alias="Правая полудлина",
    )
    Height1: float = Field(
        alias="Высота трещины в первом направлении",
    )
    Height2: float = Field(
        alias="Высота трещины во втором направлении",
    )
    Width: float = Field(
        alias="Ширина трещины FZ",
    )
    CrackAffectedZoneWidth: Optional[float] = Field(
        alias="Ширина зоны влияния трещины",
    )
    CrackBoundaryCurvature: Optional[float] = Field(
        alias="Кривизна границы трещины",
    )
    ReservoirPermeabilityMultiplier: Optional[float] = Field(
        alias="Множитель проницаемости пласта",
    )
    Permeability: Optional[float] = Field(
        alias="Проницаемость",
    )
    CrackImpactPermeability: Optional[float] = Field(
        alias="Проницаемость в зоне влияния трещины (NFZ)"
    )
    MatrixPermeability: Optional[float] = Field(
        alias="Проницаемость трещины (Матрицы)",
    )
    CrackImpactPermeability2: Optional[float] = Field(
        alias="Проницаемость в зоне влияния трещины (NFZ2)"
    )
    FractureProductivityMultiplier: Optional[float] = Field(
        alias="Множитель продуктивности трещины"
    )
    ProppantTypeName: Optional[str] = Field(
        alias="Название типа пропанта",
    )
    ProppantProperties: Optional[str] = Field(
        alias="Xарактеристика падения проницаемости",
    )
    FallPeriod: Optional[float] = Field(
        alias="Период падения проницаемости в трещине",
    )
    FlowModel: Optional[str] = Field(
        alias="Имя функции зависимости проницаемости трещины от времени"
    )


class FRACTURE_SPECSSheet(KeywordsSheet):
    keyword = FRACTURE_SPECS
