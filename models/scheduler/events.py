import datetime
from collections import defaultdict
from typing import Dict, List, Type

from pydantic import BaseModel, ConfigDict, Field

from models.scheduler import keyword


class Events(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    Comment: keyword.CommentSheet = Field(
        title="Comment Sheet",
        default_factory=keyword.CommentSheet,
    )
    WELSPECS: keyword.WELSPECSSheet = Field(
        title="WELSPECS Sheet",
        default_factory=keyword.WELSPECSSheet,
    )
    WELLTRACK: keyword.WELLTRACKSheet = Field(
        title="WELLTRACK Sheet",
        default_factory=keyword.WELLTRACKSheet,
    )
    COMPDATMD: keyword.COMPDATMDSheet = Field(
        title="COMPDATMD Sheet",
        default_factory=keyword.COMPDATMDSheet,
    )
    WSEGVALV: keyword.WSEGVALVheet = Field(
        title="WSEGVALV Sheet",
        default_factory=keyword.WSEGVALVheet,
    )
    FRACTURE_SPECS: keyword.FRACTURE_SPECSSheet = Field(
        title="FRACTURE_SPECS Sheet",
        default_factory=keyword.FRACTURE_SPECSSheet,
    )
    FRACTURE_STAGE: keyword.FRACTURE_STAGESheet = Field(
        title="FRACTURE_STAGE Sheet",
        default_factory=keyword.FRACTURE_STAGESheet,
    )
    WEFAC: keyword.WEFACSheet = Field(
        title="WEFAC Sheet",
        default_factory=keyword.WEFACSheet,
    )
    WECON: keyword.WECONSheet = Field(
        title="WECON Sheet",
        default_factory=keyword.WECONSheet,
    )
    WECONINJ: keyword.WECONINJSheet = Field(
        title="WECONINJ Sheet",
        default_factory=keyword.WECONINJSheet,
    )
    WCONPROD: keyword.WCONPRODSheet = Field(
        title="WCONPROD Sheet",
        default_factory=keyword.WCONPRODSheet,
    )
    WCONINJE: keyword.WECONINJSheet = Field(
        title="WECONINJ Sheet",
        default_factory=keyword.WECONINJSheet,
    )
    WELDRAW: keyword.WELDRAWSheet = Field(
        title="WELDRAW Sheet",
        default_factory=keyword.WELDRAWSheet,
    )
    GCONPROD: keyword.GCONPRODSheet = Field(
        title="GCONPROD Sheet",
        default_factory=keyword.GCONPRODSheet,
    )
    GCONINJE: keyword.GCONINJESheet = Field(
        title="GCONINJE Sheet",
        default_factory=keyword.GCONINJESheet,
    )
    WCONHIST: keyword.WCONHISTSheet = Field(
        title="WCONHIST Sheet",
        default_factory=keyword.WCONHISTSheet,
    )
    WCONINJH: keyword.WCONINJHSheet = Field(
        title="WCONINJH Sheet",
        default_factory=keyword.WCONINJHSheet,
    )
    WLIST: keyword.WLISTSheet = Field(
        title="WLIST Sheet",
        default_factory=keyword.WLISTSheet,
    )
    WELOPEN: keyword.WELOPENSheet = Field(
        title="WELOPEN Sheet",
        default_factory=keyword.WELOPENSheet,
    )
    GRUPTREE: keyword.GRUPTREESheet = Field(
        title="GRUPTREE Sheet",
        default_factory=keyword.GRUPTREESheet,
    )
    ARITHMETIC: keyword.ARITHMETICSheet = Field(
        title="ARITHMETIC Sheet",
        default_factory=keyword.ARITHMETICSheet,
    )
    GINJGAS: keyword.GINJGASSheet = Field(
        title="GINJGAS Sheet",
        default_factory=keyword.GINJGASSheet,
    )
    ArbitraryWord: keyword.ArbitraryWordSheet = Field(
        title="Arbitrary Word Sheet",
        default_factory=keyword.ArbitraryWordSheet,
    )

    @classmethod
    def sheet_names(cls) -> List[str]:
        results = [k for k in cls.model_fields.keys()]
        return results

    @classmethod
    def get_sheet_type(cls, name: str) -> Type[keyword.KeywordsSheet]:
        results = cls.model_fields[name].annotation
        return results

    def get_timestamps(self) -> Dict[datetime.datetime, List[Type[keyword.KeywordsSheet]]]:
        results = defaultdict(list)

        for k, v in self:
            for t in v.get_timestamps():
                results[t].append(v.__class__)

        return dict(results)
