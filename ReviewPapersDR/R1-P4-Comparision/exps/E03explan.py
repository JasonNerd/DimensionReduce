from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from ECG200Reader import get_train_data
from sklearn.preprocessing import StandardScaler
import numpy as np


ss = StandardScaler()
X_train, y_train = get_train_data()
res_path = "res/feature_hist/"
sn, fn = X_train.shape  # 样本数量, 特征数量
X_train_normed = ss.fit_transform(X_train)
# 绘制PCA特征数解释率曲线图
pca = PCA(n_components=fn)
pca.fit(X_train_normed)
evr = np.cumsum(pca.explained_variance_ratio_)
plt.plot(range(fn), evr)
plt.savefig("res/pca_evr_curve")