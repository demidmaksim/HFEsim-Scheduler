from models.scheduler import Schedule


def to_eclipse_ascii(schedule: Schedule) -> None:

    for timestamp, events in schedule.iter_timestamps():
        pass
