import pandas as pd
import json
import xml.etree.ElementTree as ET


# CSVファイルをDataFrameに読み込む
df = pd.read_csv("log_individual_pedestrians_modified.csv", dtype={"current_velocity": float})

# pedestrianIDがag05604の行を抽出して新しいDataFrameに格納
new_df = df[df['pedestrianID'] == 'ag05604']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag05604_data.csv", index=False)



# pedestrianIDがag05604の行を抽出して新しいDataFrameに格納
new_df = df[df['pedestrianID'] == 'ag10824']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag10824_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag03495']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag03594_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag01728']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag01728_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag07103']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag07103_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag05510']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag05510_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag06036']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag06036_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag08370']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag08370_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag07394']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag07394_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag00602']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag00602_data.csv", index=False)
new_df = df[df['pedestrianID'] == 'ag04386']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag04386_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag05652']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag05652_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag05241']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag05241_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag01338']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag01338_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag02315']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag02315_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag03137']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag03137_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag00200']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag00200_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag06894']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag06894_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag03542']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag03542_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag09328']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag09328_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag10117']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag10117_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag02657']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag02657_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag12688']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag12688_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag07232']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag07232_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag05339']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag05339_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag12837']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag12837_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag10393']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag10393_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag12360']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag12360_data.csv", index=False)

new_df = df[df['pedestrianID'] == 'ag11480']

# 新しいCSVファイルとして保存
new_df.to_csv("agent_individual/ag11480_data.csv", index=False)