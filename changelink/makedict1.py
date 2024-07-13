import xmltodict

xml_file_path = "map_new.xml"

#xmlファイルを読み込んで辞書に変換
with open(xml_file_path, "r") as xml_file:
    xml_data = xml_file.read()
    xml_dict = xmltodict.parse(xml_data)

#辞書の内容を確認
print(xml_dict)

new_xml_file_path = "dict_map_new.xml"

with open(new_xml_file_path,"w") as new_xml_file:
    new_xml_file.write(xmltodict.unparse(xml_dict, pretty=True))