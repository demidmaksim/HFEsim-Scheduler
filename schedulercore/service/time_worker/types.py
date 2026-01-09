import datetime
from typing import Dict, Literal, Union

import numpy as np

supported_time_types = Union[np.datetime64, datetime.datetime, Dict[Literal["month", "year"], int]]
