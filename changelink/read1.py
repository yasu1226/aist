import xml.etree.ElementTree as ET
# XMLファイルのパス
xml_file_path = "map_new.xml"
# XMLファイルを解析してルート要素を取得
tree = ET.parse(xml_file_path)
root = tree.getroot()
# Link要素の幅(width)値を抽出
for link in root.findall(".//Link"):
    width = link.get("width")
    if width is not None:
        print("Linkの幅(width):", width)
    else:
        print("Linkの幅(width)は存在しません")