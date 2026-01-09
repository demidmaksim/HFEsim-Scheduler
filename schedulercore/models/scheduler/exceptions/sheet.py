from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

    from schedulercore.service import TimeValueError


class SheetTimeValueError(ValueError):
    def __init__(self, sheet_name, row_number: int, e: "TimeValueError") -> None:
        self.sheet_name = sheet_name
        self.time = e.value
        self.row = row_number

    def __str__(self) -> str:
        msg = f"На листе {self.sheet_name} не верное время {self.time} на строке {self.row + 1}"
        return msg


class SheetValidateError(ValueError):
    def __init__(self, sheet_name: str, time: "datetime", column: str, value) -> None:
        self.sheet_name = sheet_name
        self.time = time
        self.col = column
        self.value = value

    def __str__(self) -> str:
        msg = (
            f"На листе {self.sheet_name} "
            f"в колонке {self.col} "
            f"в строке с временем {self.time} "
            f"не валидное значение {self.value}"
        )
        return msg
