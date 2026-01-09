from datetime import datetime
from typing import Any, Dict, List, Optional, Type, Union

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator
from tabulate import tabulate

from schedulercore.models.scheduler.exceptions.sheet import SheetTimeValueError, SheetValidateError
from schedulercore.service import time_worker as tw


class Keyword(BaseModel):
    time: datetime = Field(
        title="Момент времени эвента",
        alias="Time",
    )

    model_config = ConfigDict(
        extra="ignore",
    )

    def __init__(self, **data: Any) -> None:
        try:
            super().__init__(**data)
        except ValidationError as e:
            error_data = [error for error in e.errors()]
            error = SheetValidateError(
                sheet_name=self.__class__.__name__,
                time=data.get("Time", None),
                column=error_data[0].get("loc", None),
                value=error_data[0].get("input", None),
            )
            raise error

    @model_validator(mode="before")
    def force_str(cls, values, *args, **kwargs):
        alias = cls._alias()
        for k, v in values.items():
            if (aliased_k := alias.get(k, None)) is None:
                continue

            if v == "1*":
                values[k] = None

            elif cls.model_fields[aliased_k].annotation == str and not pd.isnull(v):
                values[k] = str(v)
            elif pd.isnull(v):
                values[k] = None

        return values

    @field_validator("time", mode="before")
    def validate_time(cls, value):
        return tw.convert_to_datetime(value)

    @classmethod
    def _alias(cls) -> Dict[str, str]:
        results = {v.alias: k for k, v in cls.model_fields.items()}
        return results

    @classmethod
    def time_name(cls) -> str:
        return cls.model_fields["time"].alias

    @classmethod
    def field(cls) -> List[str]:
        results = [f.alias for n, f in cls.model_fields.items()]
        return results

    def get_eclipse_string(self) -> List[Union[str, int]]:
        results = [(v if v is not None else "1*") for k, v in self if k != "time"]
        results.append("/")
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
                raise SheetTimeValueError(self.keyword.__name__, i, e)

            self._sheet.loc[i, self.keyword.time_name()] = date

    def __repr__(self) -> str:
        results = f"{self.__class__.__name__}({self._sheet.index.shape[0]})"
        return results

    def get_timestamps(self) -> List[datetime]:
        if self._sheet.empty:
            return []

        timestamps = self._sheet.loc[:, self.keyword.time_name()].values
        timestamps = pd.unique(timestamps)
        results = [tw.convert_to_datetime(t) for t in timestamps]
        return results

    def fill_file(self, file, date: datetime):
        file.write(f"{self.keyword.__name__}\n")

        results = []
        time_field_name = self.keyword.time_name()
        pattern = self._sheet.loc[:, time_field_name].values == tw.convert_to_timestemp(date)
        for i, row_data in self._sheet.loc[pattern, :].iterrows():
            row = self.keyword(**row_data)
            results.append(row.get_eclipse_string())

        string_table = tabulate(results, showindex=False, tablefmt="plain")
        file.write("  ")
        file.write(string_table.replace("\n", "\n  "))
        file.write("\n/\n\n")
        return file
