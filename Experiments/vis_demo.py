# coding='utf-8'
"""t-SNE对手写数字进行可视化"""
from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA, KernelPCA, TruncatedSVD, FastICA, NMF
from sklearn.manifold import Isomap, MDS, LocallyLinearEmbedding, SpectralEmbedding, TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import warnings
warnings.filterwarnings("ignore")  # 忽略所有警告

def get_data():
    digits = datasets.load_digits(n_class=6)
    data = digits.data
    label = digits.target
    return data, label
def plot_embedding(data, label, title):
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)
    for i in range(data.shape[0]):
        plt.text(data[i, 0], data[i, 1], str(label[i]),
                 color=plt.cm.Set1(label[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.title(title)
    plt.show()


data, label = get_data()
ss = StandardScaler()
data = ss.fit_transform(data)
print(data.shape)
print('fit start')
t0 = time()
result = LinearDiscriminantAnalysis(n_components=2).fit_transform(data, label)
print('fit end')
plot_embedding(result, label, '(time %.2fs)' % (time() - t0))
