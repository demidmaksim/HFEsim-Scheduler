from typing import Optional

from pydantic import Field

from models.keyword._abstract import Keyword, KeywordsSheet


class ArbitraryWord(Keyword):
    KeyWordName: Optional[str] = Field(
        title="Ключевое слово",
    )
    KeyWordValue: Optional[str] = Field(
        title="Строка с управляющим словами",
    )


class ArbitraryWordSheet(KeywordsSheet):
    pass
