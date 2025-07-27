from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class GINJGAS(Keyword):
    GroupName: Optional[str] = Field(
        alias="Имя группы",
    )
    GasCompound: Optional[str] = Field(
        alias="Cостав нагнетаемого газа",
    )
    CharacterString: Optional[str] = Field(
        alias="Строка символов, задающая данные в параметре 2",
    )
    CompoundName: Optional[str] = Field(
        alias="Имя композиционного состава потока",
    )
    Separator: Optional[str] = Field(
        alias="Ступень сепаратора",
    )


class GINJGASSheet(KeywordsSheet):
    keyword = GINJGAS
