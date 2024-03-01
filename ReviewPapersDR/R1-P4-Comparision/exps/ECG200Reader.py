# 读取 ECG200 数据集
import numpy as np

ecg200_path = "../data/ECG200/"
train_file_name = "ECG200_TRAIN.tsv"
test_file_name = "ECG200_TEST.tsv"

def get_data(df_path: str):
    y_label = []
    X_data = []
    with open(df_path, 'r') as df:
        for line in df:
            sample_l = line.split('\t')
            y_label.append(int(sample_l[0]))
            X_data.append(list(map(float, sample_l[1:])))
    return np.array(X_data), np.array(y_label)

def get_train_data():
    train_path = ecg200_path+train_file_name
    return get_data(train_path)

def get_test_data():
    test_path = ecg200_path+test_file_name
    return get_data(test_path)

