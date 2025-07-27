from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class FRACTURE_STAGE(Keyword):
    FracName: Optional[str] = Field(
        alias="Имя трещины",
    )
    FrackState: str = Field(
        alias="Состояние",
    )
    ArithmeticName: Optional[str] = Field(
        alias="Имя арифметики",
    )
    ProppantVolume: Optional[float] = Field(
        alias="Объем пропанта",
    )


class FRACTURE_STAGESheet(KeywordsSheet):
    keyword = FRACTURE_STAGE
