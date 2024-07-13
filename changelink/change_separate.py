import xml.etree.ElementTree as ET
import json
# XMLファイルのパス
xml_file_path = "map_new.xml"

#JSONファイルのパス
json_file_path = "input.json"

with open(json_file_path,"r") as json_file:
    data = json.load(json_file)
    
# 新しいXMLファイルのパス
new_xml_file_path = "tokyo/map/changerand_map.xml"

# XMLファイルを解析してルート要素を取得
tree = ET.parse(xml_file_path)
root = tree.getroot()
count = 0

# Link要素の幅(width)値を+n(nはincrementsの値)して新しいXMLファイルに保存
for link in root.findall(".//Link"):
    width = link.get("width")
    search_id = link.get("id")
    
    #xmlファイルのidとJSONのファイルのidで一致するものを探す
    if search_id in data:
        increments = data[search_id]["increments"]
        new_width = str(float(width) + float(increments))
        link.set("width", new_width)
        new_tag = ET.Element("tag")
        new_tag.text = "increments=" + str(float(increments))
        link.append(new_tag)
        if count < 3:
            print(f"Linkの幅(前,後): {width}, {new_width}")
            count += 1
    else:
        print("No id")
        
# 新しいXMLファイルを保存
tree.write(new_xml_file_path)


