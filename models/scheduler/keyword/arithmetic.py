from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class ARITHMETIC(Keyword):
    ArithmeticName: str = Field(
        title="Имя арифметики",
    )
    Expression: Optional[str] = Field(
        title="Выражение",
    )
    Description: Optional[str] = Field(
        title="Описание",
    )


class ARITHMETICSheet(KeywordsSheet):
    keyword = ARITHMETIC
