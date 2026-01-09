from typing import Optional

from pydantic import Field

from schedulercore.models.scheduler import Keyword, KeywordsSheet


class ArbitraryWord(Keyword):
    KeyWordName: Optional[str] = Field(
        alias="Ключевое слово",
    )
    KeyWordValue: Optional[str] = Field(
        alias="Строка с управляющим словами",
    )


class ArbitraryWordSheet(KeywordsSheet):
    keyword = ArbitraryWord
