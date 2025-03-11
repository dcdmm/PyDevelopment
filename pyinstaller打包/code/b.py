import pandas as pd
import os
import sys


def sum_ser():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # pyinstaller打包后的临时解压目录
        csv_path_d0 = os.path.join(base_path, "data", "d0.csv")
        csv_path_e0 = os.path.join(base_path, "data", "e0.csv")
        csv_path_e1 = os.path.join(base_path, "data", "e1.csv")
    else:
        base_path = os.path.dirname(__file__)  # 当前文件路径
        csv_path_d0 = os.path.join(base_path, "../data", "d0.csv")
        csv_path_e0 = os.path.join(base_path, "../extra", "e0.csv")
        csv_path_e1 = os.path.join(base_path, "../extra", "e1.csv")
    d0 = pd.read_csv(csv_path_d0, index_col=0).iloc[:, 0]
    e0 = pd.read_csv(csv_path_e0, index_col=0).iloc[:, 0]
    e1 = pd.read_csv(csv_path_e1, index_col=0).iloc[:, 0]
    return d0.sum() + e0.sum() + e1.sum()
