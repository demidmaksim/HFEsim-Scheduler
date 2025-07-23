from pathlib import Path
from typing import Dict

import pandas as pd

from models import KeywordsSheet, Schedule


def read_exel(path: Path) -> Schedule:
    row_data: Dict[str, pd.DataFrame] = pd.read_excel(
        io=path,
        sheet_name=Schedule.sheet_names(),
        header=0,
        index_col=None,
    )
    data: Dict[str, KeywordsSheet] = {k: Schedule.get_sheet_type(k)(v) for k, v in row_data.items()}
    results = Schedule(**data)
    return results
