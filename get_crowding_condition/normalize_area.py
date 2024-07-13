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

    # 上書きされたDataFrameをCSVファイルとして保存
    df.to_csv("log_individual_pedestrians_modified.csv", index=False)

    # CSVファイルをDataFrameに読み込む
    df = pd.read_csv("log_individual_pedestrians_modified.csv", dtype={"current_velocity": float})

    # JSONファイルのパス
    json_file_path = "length.json"

    with open(json_file_path, "r") as json_file:
        length_data = json.load(json_file)

    # _yで始まる行のみを抽出
    df_y = df[df["current_linkID"].str.startswith("_y")]

    # 出現回数を計算
    link_counts = df["current_linkID"].value_counts().reset_index().rename(columns={"index": "link_id", "current_linkID": "count"})
    print(link_counts)

    # _y で始まる行ごとに current_velocity が 0 でない行の割合を計算
    nonzero_ratios = {}
    for y_id, group in df_y.groupby("current_linkID"):
        nonzero_ratio = len(group[group["current_velocity"] == 0]) / len(group)
        nonzero_ratios[y_id] = nonzero_ratio


    # 単位面積当りの出現回数を計算し、リンクIDと対応する辞書に格納
    normalized_counts = {}
    data = []
    for index, row in link_counts.iterrows():
        link_id = row["link_id"]

        count = row["count"]
        length = length_data.get(link_id, {}).get("length", 0)
        width = length_data.get(link_id, {}).get("width", 0)
        area = float(length) * float(width)
        # ゼロ除算を避ける
        if length != 0 and width != 0:
            area = float(length) * float(width)
            normalized_count = count / area
            data.append([link_id, count, normalized_count])
            
    # 各current_linkIDにおいて、同じcurrent_linkIDである行を抽出し、その行すべてのcurrent_velocityの平均を計算する
    v_data = {}
    for link_id in df["current_linkID"].unique():
        velocities = df[df["current_linkID"] == link_id]["current_velocity"]
        velocity_mean = velocities.mean()
        v_data[link_id] = velocity_mean

    # 単位面積当りの出現回数の大きい順にソート
    data_sorted = sorted(data, key=lambda x: x[2], reverse=True)

    output_file = "0904/AAA.txt"
    with open(output_file, "w") as f:
        for row in data_sorted:
            velocity = v_data[row[0]]
            f.write(f"Link ID: {row[0]}, 出現回数: {row[1]}, 単位面積当りの出現回数: {row[2]:.2f}, vの平均: {velocity:.2f}\n")

   