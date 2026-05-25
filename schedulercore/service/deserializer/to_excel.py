from pathlib import Path

import xlsxwriter as xlsw

from schedulercore.models.scheduler.schedule import Events


def create_pattern(
    path: str | Path = "Pattern.xlsx",
) -> None:
    workbook = xlsw.Workbook(path)

    cell_format = workbook.add_format(
        {
            "bold": True,
            "text_wrap": True,
            "center_across": True,
            "valign": "vcenter",
            "fg_color": "#D7E4BC",
            "border": 1,
        }
    )

    for keyword, event in Events.annotations():
        sheet = workbook.add_worksheet(keyword)
        sheet.write_row(0, 0, event.fields_name(), cell_format)

    workbook.close()
