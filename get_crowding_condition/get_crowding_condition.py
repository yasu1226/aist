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

    # CSVファイルをDataFrameに読み込む
    df = pd.read_csv("log_individual_pedestrians_modified.csv", dtype={"current_velocity": float})



    # # _y450の行を抽出
    # df_y450 = df[df["current_linkID"] == "_y450"]

    # # _y450の行でcurrent_velocityが0でない行を抽出
    # df_y450_nonzero = df_y450[df_y450["current_velocity"] >= 0.3]

    # # _y450の行でcurrent_velocityが0でない行の割合を計算
    # nonzero_ratio = len(df_y450_nonzero) / len(df_y450)

    # print("current_velocityが0でない割合:", nonzero_ratio)



    # _y で始まる行のみを抽出
    df_y = df[df["current_linkID"].str.startswith("_y")]

    # 出現回数を計算
    link_counts = df["current_linkID"].value_counts()

    # _y で始まる行ごとに current_velocity が 0 でない行の割合を計算
    nonzero_ratios = {}
    for y_id, group in df_y.groupby("current_linkID"):
        nonzero_ratio = len(group[group["current_velocity"] == 0]) / len(group)
        nonzero_ratios[y_id] = nonzero_ratio

    # current_velocityが0でない割合が0.8より大きいリンクIDを抽出
    valid_links = [y_id for y_id, ratio in nonzero_ratios.items() if ratio > 0.0]

    # 出現回数でソートして上位100件を取得
    top_10_links = link_counts[link_counts.index.isin(valid_links)].sort_values(ascending=False).head(1000)


    # 上位10リンクの情報を出力
    for link_id in top_10_links.index:
        # if link_id == "_y022" or link_id =="_y027" or link_id =="_y013" or link_id =="_y079" or link_id =="_y779" or link_id =="_y691" or link_id =="_y575" or link_id =="_y1051" or link_id =="_y806":
            ratio = nonzero_ratios.get(link_id, 0)  # リンクIDに対応する割合を取得。存在しない場合は0を返す
            count = link_counts[link_id]  # リンクの出現回数を取得
            print(f"Link ID: {link_id}, 出現回数: {count}, current_velocityが0の割合: {ratio:.2f}")


    output_file = "0904/output.txt"
    # link_idをインデックスとして持つDataFrameを作成
    link_counts_df = link_counts.reset_index().rename(columns={"index": "link_id"})

    # ファイルに書き込む
    with open(output_file, "w") as f:
        for link_id in top_10_links.index:
            # リンクIDに対応する行を取得
            row = link_counts_df[link_counts_df["link_id"] == link_id].iloc[0]
            ratio = nonzero_ratios.get(link_id, 0)
            count = link_counts[link_id]  # リンクの出現回数を取得
            f.write(f"Link ID: {link_id}, 出現回数: {count}, current_velocityが0の割合: {ratio:.2f}\n")

    print("ファイルに書き込みました:", output_file)


    output_file2 = "0904/v_ratio.txt"
    # nonzero_ratios をソートして上位1000件を表示
    sorted_ratios = sorted(nonzero_ratios.items(), key=lambda x: x[1], reverse=True)
    with open(output_file2, "w") as f:
        for link_id, ratio in sorted_ratios:
            count = link_counts[link_id]  # リンクの出現回数を取得
            f.write(f"Link ID: {link_id}, current_velocityが0の割合: {ratio:.2f}, 出現回数: {count}\n")