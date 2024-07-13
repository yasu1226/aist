import xml.etree.ElementTree as ET
import random
import json

# XMLファイルのパス
xml_file_path = "yy_map.xml"

tree = ET.parse(xml_file_path)
root = tree.getroot()

x = {}

links = list(root.findall(".//Link"))

# どれか１つのlinkだけincrementsを5.0にする
new_file_path = "tag_dict.json"
for link in root.findall(".//Link"):
    ID = link.get("id")
    tag = None
    for tag_elem in link.findall("tag"):
        if tag_elem.text is not None and tag_elem.text[:2] == "_y":
            tag = tag_elem.text
            break
    width = link.get("width")
    increments = 0.0
    if width is not None:
        x[ID] = {"width": width, "increments": increments, "tag": tag}

# JSONファイルに書き込む際にキーを文字列に変換
x_str_keys = {str(key): value for key, value in x.items()}

with open(new_file_path, "w") as new_file:
    json.dump(x_str_keys, new_file, indent=4)
