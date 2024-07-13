import pandas as pd
import json
import xml.etree.ElementTree as ET

def p_id_to_y_tag(target_id, root):
    for link in root.findall(".//Link"):
        link_id = link.get("id")
        if target_id == link_id:
            for tag_elem in link.findall("tag"):
                if tag_elem.text is not None and tag_elem.text[:2] == "_y":
                    tag = tag_elem.text
                    return tag  # _yタグを見つけたらすぐに返す

    return None  # _yタグが見つからない場合

if __name__ == "__main__":
    # XMLファイルのパス
    xml_file_path = "/home/otsubo/CrowdWalk/crowdwalk/sample/tokyo/map/map_y/yy_map.xml"
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    df = pd.read_csv("/home/otsubo/CrowdWalk/crowdwalk/sample/tokyo/pro/log/log_individual_pedestrians.csv")
    link_id = df.iloc[:, 2]

    for i, target_id in enumerate(link_id):
        tag = p_id_to_y_tag(target_id, root)
        if tag is not None:
            # _yタグが見つかった場合、元のCSVファイルの2番目の列に上書きする
            df.iloc[i, 2] = tag
        # else:
        #     print("wrong")

    # 上書きされたDataFrameをCSVファイルとして保存
    df.to_csv("log_individual_pedestrians_modified.csv", index=False)