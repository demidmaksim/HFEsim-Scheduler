from typing import Type

import pandas as pd
from pydantic import BaseModel


class Keyword(BaseModel):
    pass


class KeywordsSheet:
    keyword: Type[Keyword]

    def __init__(self, sheet: pd.DataFrame) -> None:
        self._sheet = sheet
