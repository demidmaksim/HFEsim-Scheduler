from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class FRACTURE_STAGE(Keyword):
    FracName: Optional[str] = Field(
        title="Имя трещины",
    )
    FrackState: str = Field(
        title="Состояние",
    )
    ArithmeticName: Optional[str] = Field(
        title="Имя арифметики",
    )
    ProppantVolume: Optional[float] = Field(
        title="Объем пропанта",
    )


class FRACTURE_STAGESheet(KeywordsSheet):
    pass
