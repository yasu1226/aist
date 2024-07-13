import pandas as pd

df = pd.read_csv("agent_movement_history.csv")

max_arrive_time = df.iloc[:,7].max()
mean_arrive_time = df.iloc[:,7].mean()
print(max_arrive_time)
print(mean_arrive_time)