from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class ARITHMETIC(Keyword):
    ArithmeticName: str = Field(
        alias="Имя арифметики",
    )
    Expression: Optional[str] = Field(
        alias="Выражение",
    )
    Description: Optional[str] = Field(
        alias="Описание",
    )


class ARITHMETICSheet(KeywordsSheet):
    keyword = ARITHMETIC
