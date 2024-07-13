import xml.etree.ElementTree as ET
import random
import json


# XMLファイルのパス
xml_file_path = "map_new.xml"

tree = ET.parse(xml_file_path)
root = tree.getroot()


x = {}

links = list(root.findall(".//Link"))
random_link = random.choice(links)

# どれか１つのlinkだけincrementsを5.0にする
new_file_path = "newdict3.json"
for link in root.findall(".//Link"):

    ID = link.get("id")
    width = link.get("width")
    increments = 0.0
    if link == random_link:
        increments = 5.0
        print(f"the +5.0 changeed id is {ID}")
    if width is not None:
        x[ID] = {"width":width,"increments":increments}

with open(new_file_path,"w") as new_file:
    json.dump(x, new_file, indent=4)
