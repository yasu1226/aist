import os
import subprocess
import sys
import json
import pandas as pd
import ast
import matplotlib.pyplot as plt
import sys
import csv


def mk_history(df_results0, df_results1, df_results2, df_results3, df_results4, df_results5, df_results6):
    # 新しい図を作成
    plt.figure(figsize=(8, 6))
   
    # # DataFrameから反復回数ごとの最小評価時間の値を取得
    # df_results_values = df_results['time'].tolist()
    # df_results2_values = df_results2['time'].tolist()
    # df_results3_values = df_results3['time'].tolist()
    # df_results4_values = df_results4['time'].tolist()
    # df_results5_values = df_results5['time'].tolist()
    # df_results6_values = df_results6['time'].tolist()
    plt.plot(df_results0, df_results0.index, label='original', marker='o',markersize=1, linestyle='-', color='black')
    plt.plot(df_results1, df_results1.index, label='random-search_1287_+3', marker='o',markersize=1, linestyle='-', color='blue')
    plt.plot(df_results2, df_results2.index, label='random-search_1287_+5', marker='o',markersize=1, linestyle='-', color='skyblue')
    plt.plot(df_results3, df_results3.index, label='random-search_653_+3', marker='o',markersize=1, linestyle='-', color='green')
    plt.plot(df_results4, df_results4.index, label='random-search_653_+5', marker='o',markersize=1, linestyle='-', color='lightgreen')
    plt.plot(df_results5, df_results5.index, label='random-search_533_+3', marker='o',markersize=1, linestyle='-', color='red')
    plt.plot(df_results6, df_results6.index, label='random-search_533_+5', marker='o',markersize=1, linestyle='-', color='salmon')
    plt.title("max_arrive_time")
    plt.xlabel('Evacuation Time [s]')
    plt.ylabel('Number of Evacuees')
    plt.grid(True)
    plt.legend()
    
    # ラベルの背景に矩形を描画し、透明度を設定
    leg = plt.legend()
    leg.get_frame().set_alpha(1)  # 透明度を設定（0から1の間の値で指定）
    # 画像ファイルとして保存
    # plt.savefig(f'/home/otsubo/graph/0904/IIIIIIIII.png')
    plt.savefig("/home/otsubo/aist/graph/agent_history/0904_history.pdf", format='pdf')
    plt.show()


if __name__ == "__main__":
    # 実験ディレクトリ
    df0 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_original.csv")
    df1 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_1287_+3.csv")
    df2 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_1287_+5.csv")
    df3 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_653_+3.csv")
    df4 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_653_+5.csv")
    df5 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_533_+3.csv")
    df6 = pd.read_csv("/home/otsubo/aist/graph/agent_history/0904_533_+5.csv")

    df0_history = df0.iloc[:, 7]
    df1_history = df1.iloc[:, 7]
    df2_history = df2.iloc[:, 7]
    df3_history = df3.iloc[:, 7]
    df4_history = df4.iloc[:, 7]
    df5_history = df5.iloc[:, 7]
    df6_history = df6.iloc[:, 7]

    # new_df1 = pd.DataFrame(df1_history, columns=['time'])
    # new_df2 = pd.DataFrame(df2_history, columns=['time'])
    # new_df3 = pd.DataFrame(df3_history, columns=['time'])
    # new_df4 = pd.DataFrame(df4_history, columns=['time'])
    # new_df5 = pd.DataFrame(df5_history, columns=['time'])
    # new_df6 = pd.DataFrame(df6_history, columns=['time'])

    mk_history(df0_history, df1_history, df2_history, df3_history, df4_history, df5_history, df6_history)
