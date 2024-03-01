import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE

# 加载数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 使用t-SNE进行降维
tsne = TSNE(n_components=2, random_state=0)
X_tsne = tsne.fit_transform(X)

# 可视化结果
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b']
markers = ['o', 's', '^']
for i in range(3):
    plt.scatter(X_tsne[y == i, 0], X_tsne[y == i, 1], c=colors[i], marker=markers[i], label=iris.target_names[i])
plt.xlabel('t-SNE feature 1')
plt.ylabel('t-SNE feature 2')
plt.legend(loc='best')
plt.title('t-SNE visualization of Iris dataset')
plt.show()
