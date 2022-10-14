from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config

@dataclass_json()
@dataclass()
class OlsMap:
    Name: str = ""
    #IdName: str = ""
    FolderName: str = ""
    Type: str = "eZweidim"
    #ViewMode: str = "eViewText"
    #RWin: str = "eBars"
    DataOrg: str = "eLoHi"

    #bReciprocal: str = "0"
    bSigned: str = "1"
    #bDelta: str = "0"
    #bPercent: str = "0"
    #bOriginal: str = "0"
    #bOriginalValues: str = "0"

    Columns: str = "0"
    Rows: str = "0"
    Radix: str = "10"
    Comment: str = "0"
    Precision: str = "2"
    #SkipBytes: str = "0"
    #LineSkipBytes: str = "0"

    Map_Name: str = field(default="", metadata=config(field_name="Fieldvalues.Name"))
    Map_Unit: str = field(default="0", metadata=config(field_name="Fieldvalues.Unit"))
    Map_Factor: str = field(default="0", metadata=config(field_name="Fieldvalues.Factor"))
    Map_Offset: str = field(default="0", metadata=config(field_name="Fieldvalues.Offset"))
    Map_StartAddr: str = field(default="0", metadata=config(field_name="Fieldvalues.StartAddr"))

    X_Name: str = field(default="", metadata=config(field_name="AxisX.Name"))
    #X_IdName: str = field(default="", metadata=config(field_name="AxisX.IdName"))
    X_Unit: str = field(default="0", metadata=config(field_name="AxisX.Unit"))
    X_Factor: str = field(default="0", metadata=config(field_name="AxisX.Factor"))
    X_Offset: str = field(default="0", metadata=config(field_name="AxisX.Offset"))
    X_Radix: str = field(default="10", metadata=config(field_name="AxisX.Radix"))
    #X_bBackwards: str = field(default="0", metadata=config(field_name="AxisX.bBackwards"))
    #X_bReciprocal: str = field(default="0", metadata=config(field_name="AxisX.bReciprocal"))
    X_bSigned: str = field(default="1", metadata=config(field_name="AxisX.bSigned"))
    X_Precision: str = field(default="2", metadata=config(field_name="AxisX.Precision"))
    X_DataSrc: str = field(default="eRom", metadata=config(field_name="AxisX.DataSrc"))
    X_DataHeader: str = field(default="4", metadata=config(field_name="AxisX.DataHeader"))
    X_DataAddr: str = field(default="0", metadata=config(field_name="AxisX.DataAddr"))
    X_DataOrg: str = field(default="eLoHi", metadata=config(field_name="AxisX.DataOrg"))
    #X_SignatureByte: str = field(default="0", metadata=config(field_name="AxisX.SignatureByte"))
    #X_SkipBytes: str = field(default="0", metadata=config(field_name="AxisX.SkipBytes"))

    Y_Name: str = field(default="", metadata=config(field_name="AxisY.Name"))
    #Y_IdName: str = field(default="", metadata=config(field_name="AxisY.IdName"))
    Y_Unit: str = field(default="0", metadata=config(field_name="AxisY.Unit"))
    Y_Factor: str = field(default="0", metadata=config(field_name="AxisY.Factor"))
    Y_Offset: str = field(default="0", metadata=config(field_name="AxisY.Offset"))
    Y_Radix: str = field(default="10", metadata=config(field_name="AxisY.Radix"))
    #Y_bBackwards: str = field(default="0", metadata=config(field_name="AxisY.bBackwards"))
    #Y_bReciprocal: str = field(default="0", metadata=config(field_name="AxisY.bReciprocal"))
    Y_bSigned: str = field(default="1", metadata=config(field_name="AxisY.bSigned"))
    Y_Precision: str = field(default="2", metadata=config(field_name="AxisY.Precision"))
    Y_DataSrc: str = field(default="eRom", metadata=config(field_name="AxisY.DataSrc"))
    Y_DataHeader: str = field(default="4", metadata=config(field_name="AxisY.DataHeader"))
    Y_DataAddr: str = field(default="0", metadata=config(field_name="AxisY.DataAddr"))
    Y_DataOrg: str = field(default="eLoHi", metadata=config(field_name="AxisY.DataOrg"))
    #Y_SignatureByte: str = field(default="0", metadata=config(field_name="AxisY.SignatureByte"))
    #Y_SkipBytes: str = field(default="0", metadata=config(field_name="AxisY.SkipBytes"))