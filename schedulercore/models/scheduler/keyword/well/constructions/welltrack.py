from datetime import datetime
from typing import Optional, Tuple

from pydantic import Field
from tabulate import tabulate

from schedulercore.models.scheduler import Keyword, KeywordsSheet
from schedulercore.service import time_worker as tw


class WELLTRACK(Keyword):
    WellName: Optional[str] = Field(
        alias="Имя скважины",
    )
    BoreName: Optional[int] = Field(
        alias="Номер ствола",
    )
    PointNumber: Optional[int] = Field(
        alias="Порядковый номер точки",
    )
    X: Optional[float] = Field(
        alias="X",
    )
    Y: Optional[float] = Field(
        alias="Y",
    )
    Z: Optional[float] = Field(
        alias="Z",
    )
    MD: Optional[float] = Field(
        alias="MD",
    )

    @classmethod
    def objects_field_name(cls) -> Tuple[str, str]:
        return cls.model_fields["WellName"].alias, cls.model_fields["BoreName"].alias


class WELLTRACKSheet(KeywordsSheet):
    keyword = WELLTRACK

    def fill_file(self, file, date: datetime):

        time_field_name = self.keyword.time_name()
        pattern = self._sheet.loc[:, time_field_name].values == tw.convert_to_timestemp(date)
        date_sheet = self._sheet.loc[pattern, :]

        key_names = self.keyword.objects_field_name()
        for i, row_data in date_sheet.loc[:, key_names].drop_duplicates().iterrows():
            pattern1 = date_sheet.loc[:, key_names[0]].values == row_data[key_names[0]]
            pattern2 = date_sheet.loc[:, key_names[1]].values == row_data[key_names[1]]
            pattern = pattern1 & pattern2
            well_sheet = date_sheet.loc[pattern, :]
            well_sheet.sort_values(by="Порядковый номер точки", inplace=True)
            data = well_sheet.loc[:, ["X", "Y", "Z", "MD"]].values

            wn = well_sheet.loc[:, key_names[0]].iloc[0]
            bn = well_sheet.loc[:, key_names[1]].iloc[0]

            if bn == 0:
                title = f"{self.keyword.__name__} '{wn}'\n"
            else:
                title = f"{self.keyword.__name__} '{wn}':{bn}\n"

            file.write(title)
            string_table = tabulate(data, showindex=False, tablefmt="plain", floatfmt=".2f")

            file.write("  ")
            file.write(string_table.replace("\n", "\n  "))
            file.write("\n/\n\n")

        return file
