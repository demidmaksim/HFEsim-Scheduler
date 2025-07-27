from typing import TYPE_CHECKING, Union

from dateutil.relativedelta import relativedelta

from service.time_worker.convertors import convert_to_datetime64

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd


def add_months(
    date: Union["np.datetime64", "pd.Timestamp"],
    count_of_month: int,
) -> "np.datetime64":
    date_np = convert_to_datetime64(date).astype("M8[ms]").astype("O")
    date_new = date_np + relativedelta(months=count_of_month)
    results = convert_to_datetime64(date_new)
    return results
