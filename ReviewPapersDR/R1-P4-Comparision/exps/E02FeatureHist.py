# 训练集每个特征的分布直方图
from matplotlib import pyplot as plt
from ECG200Reader import get_train_data
import os

X_train, y_train = get_train_data()
res_path = "res/feature_hist/"
if not os.path.exists(res_path):
    os.makedirs(res_path)
sn, fn = X_train.shape  # 样本数量, 特征数量
for i in range(fn):
    plt.hist(X_train[:,i], bins=20)
    plt.savefig(res_path+"Feature_"+str(i).zfill(3)+".png")
    plt.close()

