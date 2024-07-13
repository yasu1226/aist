import xml.etree.ElementTree as ET
# XMLファイルのパス
xml_file_path = "map_new.xml"
# 新しいXMLファイルのパス
new_xml_file_path = "changemap/allwidth_+2.xml"
# XMLファイルを解析してルート要素を取得
tree = ET.parse(xml_file_path)
root = tree.getroot()
# Link要素の幅(width)値を+1して新しいXMLファイルに保存
for link in root.findall(".//Link"):
    width = link.get("width")
    if width is not None:
        new_width = str(float(width) + 2)  # 幅を+1した値
        if float(new_width) <= 0.0:
            new_width = "1.0"
        link.set("width", new_width)  # 幅を新しい値に設定
# 新しいXMLファイルを保存
tree.write(new_xml_file_path)