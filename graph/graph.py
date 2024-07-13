import os
import subprocess
import sys
import json
import pandas as pd
import ast
import matplotlib.pyplot as plt
import sys
import csv


def mk_history(df_results, df_results2, df_results3, df_results4, df_results5, df_results6):
    # 新しい図を作成
    plt.figure(figsize=(8, 6))
    # y=1863の直線を追加1594
    plt.axhline(y=1863, color='black', linestyle='--', label='original')
   
    # DataFrameから反復回数ごとの最小評価時間の値を取得
    df_results_values = df_results['time'].tolist()
    df_results2_values = df_results2['time'].tolist()
    df_results3_values = df_results3['time'].tolist()
    df_results4_values = df_results4['time'].tolist()
    df_results5_values = df_results5['time'].tolist()
    df_results6_values = df_results6['time'].tolist()
   
    plt.plot(range(1, len(df_results_values) + 1), df_results_values, label='E_1287_+3', marker='o',markersize=1, linestyle='-', color='blue')
    plt.plot(range(1, len(df_results2_values) + 1), df_results2_values, label='E_1287_+5', marker='o',markersize=1, linestyle='-', color='skyblue')
    plt.plot(range(1, len(df_results3_values) + 1), df_results3_values, label='C_653_+3', marker='o',markersize=1, linestyle='-', color='green')
    plt.plot(range(1, len(df_results4_values) + 1), df_results4_values, label='C_653_+5', marker='o',markersize=1, linestyle='-', color='lightgreen')
    plt.plot(range(1, len(df_results5_values) + 1), df_results5_values, label='C\'_544_+3', marker='o',markersize=1, linestyle='-', color='red')
    plt.plot(range(1, len(df_results6_values) + 1), df_results6_values, label='C\'_544_+5', marker='o',markersize=1, linestyle='-', color='salmon')
    # plt.title("max_arrive_time")
    
    plt.xlabel('Iteration',fontsize=16)
    plt.ylabel('Minimum evaluate time [s]',fontsize=16)
    plt.tick_params(axis='both', labelsize=14)


    plt.grid(True)
    plt.legend()
    plt.ylim(None,1900)
    # ラベルの背景に矩形を描画し、透明度を設定
    leg = plt.legend()
    leg.get_frame().set_alpha(0)  # 透明度を設定（0から1の間の値で指定）
    # 画像ファイルとして保存
    # plt.savefig(f'/home/otsubo/graph/0901/IIIIIIIII.png')
    plt.legend(loc='upper right', bbox_to_anchor=(1,0.75))
    plt.savefig("/home/otsubo/aist/graph/0901_ave_new.pdf", format='pdf')
    plt.show()


if __name__ == "__main__":
    # 実験ディレクトリ
    df1 = pd.read_csv("/home/otsubo/aist/graph/0901/0901_1287_+3_ave5.csv")
    df2 = pd.read_csv("/home/otsubo/aist/graph/0901/0901_1287_+5_ave5.csv")
    df3 = pd.read_csv("/home/otsubo/aist/graph/0901/0901_653_+3_ave5.csv")
    df4 = pd.read_csv("/home/otsubo/aist/graph/0901/0901_653_+5_ave5.csv")
    df5 = pd.read_csv("/home/otsubo/aist/graph/0901/0901_544_+3_ave5.csv")
    df6 = pd.read_csv("/home/otsubo/aist/graph/0901/0901_544_+5_ave5.csv")

    mk_history(df1, df2, df3, df4, df5, df6)
