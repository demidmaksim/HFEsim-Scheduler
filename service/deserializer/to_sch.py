import io
import shutil
from datetime import datetime
from pathlib import Path
from typing import Union

from models.scheduler import Schedule, keyword
from service import time_worker as tw

__GENERATED_BY = "-- Generated : ScheduleCreator"


def __add_title(file: io.StringIO) -> io.StringIO:
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = (
        f"--ScheduleCreator\n"
        f"--Email:   Demid.Maksim@gmail.com\n"
        f"--GitHub:  https://github.com/demidmaksim\n"
        f"--Created: {t}\n\n\n"
    )

    file.write(title)
    return file


def __get_dates_keyword(time: tw.supported_time_types, file: io.StringIO) -> io.StringIO:
    time = tw.convert_to_datetime(time)
    str_time = time.strftime("%d %b %Y %H:%M:%S")
    results = f"DATES\t\t\t\t\t\t\t\t__GENERATED_BY \n  {str_time}\t/\n/\n\n"
    file.write(results)
    return file


def to_eclipse_ascii(
    schedule: Schedule,
    path: Union[str, Path] = "Results.sch",
) -> None:
    file = io.StringIO()
    file = __add_title(file)

    for timestamp, events in schedule.iter_timestamps():
        file = __get_dates_keyword(timestamp, file)

        for event_type in events:
            sheet = schedule.events.get_sheet(event_type)

            if isinstance(sheet, keyword.WELLTRACKSheet):
                continue

            file = sheet.fill_file(file, timestamp)

    with open(path, "w") as file_on_drive:
        file.seek(0)
        shutil.copyfileobj(file, file_on_drive)
