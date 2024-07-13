import os
import subprocess
import sys
import json
import pandas as pd
import ast
import matplotlib.pyplot as plt
import sys
import csv


def mk_history(df1_std, df2_std, df3_std, df4_std, df5_std, df6_std, df1_ave, df2_ave, df3_ave, df4_ave, df5_ave, df6_ave):
    # 新しい図を作成
    plt.figure(figsize=(8, 6))
    # y=1863の直線を追加
    plt.axhline(y=1594, color='black', linestyle='--', label='original')

    std1 = df1_std["time"]
    std2 = df2_std["time"]
    std3 = df3_std["time"]
    std4 = df4_std["time"]
    std5 = df5_std["time"]
    std6 = df6_std["time"]

    ave1 = df1_ave["time"]
    ave2 = df2_ave["time"]
    ave3 = df3_ave["time"]
    ave4 = df4_ave["time"]
    ave5 = df5_ave["time"]
    ave6 = df6_ave["time"]

    

   
    plt.plot(range(1, len(ave1) + 1), ave1, label='1287_+3', marker='o', markersize=1, linestyle='-', color='blue')
    plt.errorbar(range(1, len(ave1) + 1), ave1, yerr=std1, fmt='o', markersize=1, linestyle='-', color='blue', alpha=0.03)

    plt.plot(range(1, len(ave2) + 1), ave2, label='1287_+5', marker='o', markersize=1, linestyle='-', color='skyblue')
    plt.errorbar(range(1, len(ave2) + 1), ave2, yerr=std2, fmt='o', markersize=1, linestyle='-', color='skyblue', alpha=0.03)

    plt.plot(range(1, len(ave3) + 1), ave3, label='653_+3', marker='o', markersize=1, linestyle='-', color='green')
    plt.errorbar(range(1, len(ave3) + 1), ave3, yerr=std3, fmt='o', markersize=1, linestyle='-', color='green', alpha=0.03)

    plt.plot(range(1, len(ave4) + 1), ave4, label='653_+5', marker='o', markersize=1, linestyle='-', color='lightgreen')
    plt.errorbar(range(1, len(ave4) + 1), ave4, yerr=std4, fmt='o', markersize=1, linestyle='-', color='lightgreen', alpha=0.03)

    plt.plot(range(1, len(ave5) + 1), ave5, label='533_+3', marker='o', markersize=1, linestyle='-', color='red')
    plt.errorbar(range(1, len(ave5) + 1), ave5, yerr=std5, fmt='o', markersize=1, linestyle='-', color='red', alpha=0.03)

    plt.plot(range(1, len(ave6) + 1), ave6, label='533_+5', marker='o', markersize=1, linestyle='-', color='salmon')
    plt.errorbar(range(1, len(ave6) + 1), ave6, yerr=std6, fmt='o', markersize=1, linestyle='-', color='salmon', alpha=0.03)


    
    plt.title("max_arrive_time")
    plt.xlabel('Iteration')
    plt.ylabel('Minimum evaluate time')
    plt.grid(True)
    plt.legend()
    plt.ylim(None,1600)
    # ラベルの背景に矩形を描画し、透明度を設定
    leg = plt.legend()
    leg.get_frame().set_alpha(1)  # 透明度を設定（0から1の間の値で指定）
    # 画像ファイルとして保存
    # plt.savefig(f'/home/otsubo/graph/0904/IIIIIIIII.png')
    plt.savefig("/home/otsubo/aist/graph/0904/0904_std.pdf", format='pdf')
    plt.show()



if __name__ == "__main__":
    # 実験ディレクトリ
    df1_std = pd.read_csv("/home/otsubo/aist/graph/0904/0904_1287_+3_ave3_std.csv")
    df2_std = pd.read_csv("/home/otsubo/aist/graph/0904/0904_1287_+5_ave5_std.csv")
    df3_std = pd.read_csv("/home/otsubo/aist/graph/0904/0904_653_+3_ave5_std.csv")
    df4_std = pd.read_csv("/home/otsubo/aist/graph/0904/0904_653_+5_ave5_std.csv")
    df5_std = pd.read_csv("/home/otsubo/aist/graph/0904/0904_533_+3_ave5_std.csv")
    df6_std = pd.read_csv("/home/otsubo/aist/graph/0904/0904_533_+5_ave5_std.csv")

    df1_ave = pd.read_csv("/home/otsubo/aist/graph/0904/0904_1287_+3_ave3.csv")
    df2_ave = pd.read_csv("/home/otsubo/aist/graph/0904/0904_1287_+5_ave5.csv")
    df3_ave = pd.read_csv("/home/otsubo/aist/graph/0904/0904_653_+3_ave5.csv")
    df4_ave = pd.read_csv("/home/otsubo/aist/graph/0904/0904_653_+5_ave5.csv")
    df5_ave = pd.read_csv("/home/otsubo/aist/graph/0904/0904_533_+3_ave5.csv")
    df6_ave = pd.read_csv("/home/otsubo/aist/graph/0904/0904_533_+5_ave5.csv")

    mk_history(df1_std, df2_std, df3_std, df4_std, df5_std, df6_std, df1_ave, df2_ave, df3_ave, df4_ave, df5_ave, df6_ave)
