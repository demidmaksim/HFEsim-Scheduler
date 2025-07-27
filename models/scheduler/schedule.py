import datetime
from typing import Iterable, Optional, Tuple

from pydantic import BaseModel, Field

from models.scheduler import keyword
from models.scheduler.events import Events
from models.scheduler.time_step import TimeSteps


class Schedule(BaseModel):

    events: Events = Field(
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
        event_steps = self.events.get_timestamps()
        time_steps = self.time.get_timestamps()
        time_steps.extend(event_steps.keys())
        time_steps.sort()

        for ts in time_steps:
            yield ts, event_steps.get(ts, [])
