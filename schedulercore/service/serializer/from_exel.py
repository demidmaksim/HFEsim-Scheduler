from pathlib import Path
from typing import Dict, Union

import pandas as pd

from schedulercore.models import Events, KeywordsSheet


def read_exel(path: Union[Path, str]) -> Events:
    xls = pd.ExcelFile(path)
    xlsx_sheets = xls.sheet_names
    famous_sheets = Events.sheet_names()
    target_sheets = [s for s in xlsx_sheets if s in famous_sheets]

    row_data: Dict[str, pd.DataFrame] = pd.read_excel(
        io=path,
        sheet_name=target_sheets,
        header=0,
        index_col=None,
    )
    data: Dict[str, KeywordsSheet] = {k: Events.get_sheet_type(k)(v) for k, v in row_data.items()}
    results = Events(**data)
    return results
