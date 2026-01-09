import datetime
from typing import Iterable, List, Union

import numpy as np
import pandas as pd

from schedulercore.service.time_worker.exception import bug_catcher
from schedulercore.service.time_worker.types import supported_time_types


def convert_from_str(value: str) -> datetime.datetime:
    results = datetime.datetime.strptime(value, "%d.%m.%Y")
    return results


@bug_catcher
def convert_to_datetime64(value: supported_time_types, time_format: str = "s") -> np.datetime64:
    if isinstance(value, str):
        value = convert_from_str(value)

    if isinstance(value, np.datetime64):
        results = np.datetime64(value, time_format)
    elif isinstance(value, (datetime.datetime, datetime.date, pd.Timestamp)):
        str_value = value.strftime("%Y-%m-%d %H:%M:%S")
        results = np.datetime64(str_value, time_format)
    elif isinstance(value, dict):
        value = pd.Timestamp(month=value["month"], year=value["year"], day=1)
        results = convert_to_datetime64(value, time_format)
    else:
        raise NotImplementedError(f"Cannot convert {type(value)} to datetime64")
    return results


@bug_catcher
def convert_to_timestemp(value: supported_time_types) -> pd.Timestamp:
    if isinstance(value, pd.Timestamp):
        return value

    if isinstance(value, pd.Period):
        return value.to_timestamp()

    if not isinstance(value, np.datetime64):
        value = convert_to_datetime64(value)

    results = pd.Timestamp(value)
    return results


@bug_catcher
def convert_to_gui_time(
    value: Union[np.datetime64, pd.Timestamp, Iterable],
) -> Union[int, List[int]]:
    if isinstance(value, Iterable):
        results = [convert_to_gui_time(t) for t in value]
    else:
        results = convert_to_timestemp(value).value / 1e9

    return results


@bug_catcher
def convert_to_datetime(value: supported_time_types) -> datetime.datetime:

    if isinstance(value, datetime.datetime) and not isinstance(value, pd.Timestamp):
        return value

    numpy_value = convert_to_datetime64(value)
    results = datetime.datetime.strptime(str(numpy_value), "%Y-%m-%dT%H:%M:%S")
    return results
