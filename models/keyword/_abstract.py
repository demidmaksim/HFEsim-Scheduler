from typing import Optional, Type

import pandas as pd
from pydantic import BaseModel


class Keyword(BaseModel):
    pass


class KeywordsSheet:
    keyword: Type[Keyword]

    def __init__(self, sheet: Optional[pd.DataFrame] = None) -> None:
        self._sheet = sheet if sheet else pd.DataFrame(columns=[self.keyword.field()])
