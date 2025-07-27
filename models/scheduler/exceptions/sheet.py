from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from service.time_worker.exception import TimeValueError


class SheetValueError(ValueError):
    def __init__(self, sheet_name, row_number: int, e: "TimeValueError") -> None:
        self.sheet_name = sheet_name
        self.time = e.value
        self.row = row_number

    def __str__(self) -> str:
        msg = f"На листе {self.sheet_name} не верное время {self.time} на строке {self.row}"
        return msg
