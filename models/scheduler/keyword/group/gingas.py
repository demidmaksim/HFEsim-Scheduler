from typing import Optional

from pydantic import Field

from models.scheduler.keyword._abstract import Keyword, KeywordsSheet


class GINJGAS(Keyword):
    GroupName: Optional[str] = Field(
        title="Имя группы",
    )
    GasCompound: Optional[str] = Field(
        title="Cостав нагнетаемого газа",
    )
    CharacterString: Optional[str] = Field(
        title="Строка символов, задающая данные в параметре 2",
    )
    CompoundName: Optional[str] = Field(
        title="Имя композиционного состава потока",
    )
    Separator: Optional[str] = Field(
        title="Ступень сепаратора",
    )


class GINJGASSheet(KeywordsSheet):
    keyword = GINJGAS
