from datetime import datetime
from typing import List, Optional, Type

import pandas as pd
from pydantic import BaseModel, Field, field_validator

from models.scheduler.exceptions.sheet import SheetValueError
from service import time_worker as tw


class Keyword(BaseModel):
    time: datetime = Field(
        title="Момент времени эвента",
        alias="Time",
    )

    @field_validator("time", mode="before")
    def validate_time(cls, value):
        return value

    @classmethod
    def time_name(cls) -> str:
        return cls.model_fields["time"].alias

    @classmethod
    def field(cls) -> List[str]:
        results = [f.alias for n, f in cls.model_fields.items()]
        return results


class KeywordsSheet:
    keyword: Type[Keyword]

    def __init__(self, sheet: Optional[pd.DataFrame] = None) -> None:
        if sheet is None:
            sheet = pd.DataFrame(columns=[self.keyword.field()])
        else:
            sheet.dropna(how="all", inplace=True)

        self._sheet = sheet

        for i, row in self._sheet.iterrows():
            try:
                date = tw.convert_to_timestemp(row.loc[self.keyword.time_name()])
            except tw.TimeValueError as e:
                raise SheetValueError(self.keyword.__name__, i, e)

            self._sheet.loc[i, self.keyword.time_name()] = date

    def get_timestamps(self) -> List[datetime]:
        if self._sheet.empty:
            return []

        timestamps = self._sheet.loc[:, self.keyword.time_name()].values
        timestamps = pd.unique(timestamps)
        results = [tw.convert_to_datetime(t) for t in timestamps]
        return results
