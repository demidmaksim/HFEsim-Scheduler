from pathlib import Path
from typing import Dict

import pandas as pd

from models import Events, KeywordsSheet


def read_exel(path: Path) -> Events:
    row_data: Dict[str, pd.DataFrame] = pd.read_excel(
        io=path,
        sheet_name=Events.sheet_names(),
        header=0,
        index_col=None,
    )
    data: Dict[str, KeywordsSheet] = {k: Events.get_sheet_type(k)(v) for k, v in row_data.items()}
    results = Events(**data)
    return results
