from datetime import datetime
from typing import List, Optional, Type

import pandas as pd
from pydantic import BaseModel, Field


class Keyword(BaseModel):
    time: datetime = Field(title="момент времени эвента")


class KeywordsSheet:
    keyword: Type[Keyword]

    def __init__(self, sheet: Optional[pd.DataFrame] = None) -> None:
        self._sheet = sheet if sheet else pd.DataFrame(columns=[self.keyword.field()])

    def get_timestamps(self) -> List[datetime]:
        if self._sheet.empty:
            return []

        timestamps = self._sheet.loc[:, [self.keyword.time]].values
        timestamps = pd.unique(timestamps)
        results = timestamps.tolist()
        return results
