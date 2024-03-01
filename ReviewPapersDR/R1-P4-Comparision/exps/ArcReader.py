# 读取 Arcene 数据集
import numpy as np

arcene_root = "../data/Arcene/ARCENE/"
arcene_train_X = "arcene_train.data"
arcene_train_y = "arcene_train.labels"
arcene_test_X = "arcene_valid.data"
arcene_test_y = "arcene_valid.labels"

def get_data(df_path: str):
    X_data = []
    with open(df_path, 'r') as df:
        for line in df:
            line = line.strip()
            sample_l = line.split(' ')
            X_data.append(list(map(float, sample_l)))
    return np.array(X_data)

def get_label(df_path: str):
    y_label = []
    with open(df_path, 'r') as df:
        for line in df:
            y_label.append(float(line))
    return np.array(y_label)

def get_train_data():
    return get_data(arcene_root+arcene_train_X), get_label(arcene_root+arcene_train_y)

def get_test_data():
    return get_data(arcene_root+arcene_test_X), get_label(arcene_root+arcene_test_y)

