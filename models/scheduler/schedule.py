import datetime
from typing import Iterable, Optional, Tuple

from events import Events
from pydantic import BaseModel, Field
from time_step import TimeSteps

from models.scheduler import keyword


class Schedule(BaseModel):

    event: Events = Field(
        title="",
        default_factory=Events,
    )
    time: TimeSteps = Field(
        title="",
        default_factory=TimeSteps,
    )

    def iter_timestamps(
        self,
    ) -> Iterable[Tuple[datetime.datetime, Optional[keyword.KeywordsSheet]]]:
        event_steps = self.event.get_timestamps()
        time_steps = self.time.get_timestamps()
        time_steps.extend(event_steps.keys())
        time_steps.sort()

        for ts in time_steps:
            yield ts, event_steps.get(ts, [])
