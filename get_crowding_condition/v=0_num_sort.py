import pandas as pd
import os

# 29のCSVファイルのパス
file_paths = [

    "agent_individual/ag05604_data.csv",
    "agent_individual/ag10824_data.csv",
    "agent_individual/ag03594_data.csv",
    "agent_individual/ag01728_data.csv",
    "agent_individual/ag07103_data.csv",
    "agent_individual/ag05510_data.csv",
    "agent_individual/ag06036_data.csv",
    "agent_individual/ag08370_data.csv",
    "agent_individual/ag07394_data.csv",
    "agent_individual/ag00602_data.csv",
    "agent_individual/ag04386_data.csv",
    "agent_individual/ag05652_data.csv",
    "agent_individual/ag05241_data.csv",
    "agent_individual/ag01338_data.csv",
    "agent_individual/ag02315_data.csv",
    "agent_individual/ag03137_data.csv",
    "agent_individual/ag00200_data.csv",
    "agent_individual/ag06894_data.csv",
    "agent_individual/ag03542_data.csv",
    "agent_individual/ag09328_data.csv",
    "agent_individual/ag10117_data.csv",
    "agent_individual/ag02657_data.csv",
    "agent_individual/ag12688_data.csv",
    "agent_individual/ag07232_data.csv",
    "agent_individual/ag05339_data.csv",
    "agent_individual/ag12837_data.csv",
    "agent_individual/ag10393_data.csv",
    "agent_individual/ag12360_data.csv",
    "agent_individual/ag11480_data.csv"

    # 他のファイルのパスも同様に追加してください
]

# 各ファイルからcurrent_linkIDごとにcurrent_velocityが0である行数を取得
link_row_counts = {}

for file_path in file_paths:
    file_name = os.path.basename(file_path).split('.')[0]  # ファイル名（拡張子なし）
    df = pd.read_csv(file_path)
    grouped = df[df['current_velocity'] == 0].groupby('current_linkID').size()
    for link_id, row_num in grouped.items():
        if link_id not in link_row_counts:
            link_row_counts[link_id] = []
        link_row_counts[link_id].append((file_name, row_num))

# 各link_idのファイルごとの行数を合計
link_total_row_counts = {link_id: sum([count for _, count in counts]) for link_id, counts in link_row_counts.items()}

# 行数の大きい順にソート
sorted_links = sorted(link_total_row_counts.items(), key=lambda x: x[1], reverse=True)

# 結果をCSVファイルに書き込み
output_file = "link_row_counts.csv"
with open(output_file, "w") as f:
    f.write("link_id,row_num\n")
    for link_id, row_num in sorted_links:
        f.write(f"{link_id},{row_num}\n")
