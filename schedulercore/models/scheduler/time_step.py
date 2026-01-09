import datetime
from typing import List, Literal

import numpy as np
from pydantic import BaseModel, Field

from schedulercore.service import time_worker as tw


class TimeSteps(BaseModel):

    start: datetime.datetime = Field(
        title="",
        default_factory=datetime.datetime.now,
    )
    end: datetime.datetime = Field(
        title="",
        default_factory=lambda: datetime.datetime.now() + datetime.timedelta(days=365),
    )
    steps: Literal["h", "d", "M"] = Field(
        title="",
        default="M",
    )

    def get_timestamps(self) -> List[datetime.datetime]:
        time = np.arange(self.start, self.end, dtype=f"datetime64[{self.steps}]")
        results = [tw.convert_to_datetime(t) for t in time]
        return results
