import datetime
from typing import List, Literal

import numpy as np
from pydantic import BaseModel, Field


class TimeSteps(BaseModel):

    start: datetime.datetime = Field(
        title="",
        default=datetime.datetime.now(),
    )
    end: datetime.datetime = Field(
        title="",
        default=datetime.datetime.now() + datetime.timedelta(days=365),
    )
    steps: Literal["h", "d", "M"] = Field(
        title="",
        default="D",
    )

    def get_timestamps(self) -> List[datetime.datetime]:
        time = np.arange(self.start, self.end, dtype=f"datetime64[{self.steps}]")
        return list(time)
