import clr
import re
import os
import sys


def cwd():
    return os.path.dirname(os.path.realpath(__file__))


from olscollection import OlsCollection
from olsmap import OlsMap

clr.AddReference(cwd() + "/lib/EDCSuite.Parsers")
clr.AddReference(cwd() + "/lib/EDCSuiteBaseLibrary")

import EDCSuiteParsers
import EDCSuiteBaseLibrary


def tohex(i):
    return str(hex(i)).replace("0x", "$").upper()


def get_maps_as_olscollection(filename: str):
    filetype = str(EDCSuiteBaseLibrary.Tools().DetermineFileType(filename, True))
    print(">> Identified {} as {}".format(filename, filetype))

    parser = getattr(EDCSuiteParsers, filetype + "FileParser")()
    result = parser.parseFile(filename, None, None)

    maps = []

    for x in result[0]:
        map = OlsMap()
        map.Name = re.sub("\s?\[codeblock \d\]", "", x.Varname)
        map.FolderName = "CodeBlock {} | {}".format(x.CodeBlock, x.Subcategory)
        map.Columns = str(x.Y_axis_length)
        map.Rows = str(x.X_axis_length)
        map.Comment = x.Description
        map.Map_Name = map.Name
        map.Map_Unit = re.sub("\((.*)\)", r"\1", map.Name)
        map.Map_Factor = str(x.Correction)
        map.Map_Offset = str(x.Offset)
        map.Map_StartAddr = tohex(x.Flash_start_address)

        map.X_Name = x.X_axis_descr
        map.X_Unit = x.XaxisUnits
        map.X_Factor = str(x.X_axis_correction)
        map.X_Offset = str(x.X_axis_offset)
        map.X_DataAddr = tohex(x.Y_axis_address)

        map.Y_Name = x.Y_axis_descr
        map.Y_Unit = x.YaxisUnits
        map.Y_Factor = str(x.Y_axis_correction)
        map.Y_Offset = str(x.Y_axis_offset)
        map.Y_DataAddr = tohex(x.X_axis_address)

        maps.append(map)

    print(">> Identified {} maps in total".format(len(maps)))

    mapcoll = OlsCollection()
    mapcoll.maps = maps

    return mapcoll


if __name__ == '__main__':
    inputfile = sys.argv[1]
    with open(cwd() + '/maps.json', 'w') as f:
        f.write(OlsCollection.to_json(get_maps_as_olscollection(inputfile), indent=2))
        print(">> Written maps to maps.json. You can now import it in WinOLS.")
